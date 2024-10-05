import os
import sqlite3
from collections import defaultdict
from contextlib import closing
from datetime import datetime
from operator import itemgetter

from flask import Flask, flash, redirect, render_template, send_file, session, url_for
from forms import RegistroForm, RespostaForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "umachavesupersecretatopadaaqui"


def get_db_connection():
    conn = sqlite3.connect("ctf_pandas.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    form = RegistroForm()
    if "user_id" in session:
        return redirect(url_for("desafio"))

    if form.validate_on_submit():
        with closing(get_db_connection()) as conn:
            with conn:  # This automatically commits or rolls back
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT id, nome FROM usuarios WHERE nome = ? AND modulo = ?",
                    (form.nome.data, form.modulo.data),
                )
                user = cursor.fetchone()

                if user:
                    session["user_id"] = user["id"]
                    session["nome"] = user["nome"]
                else:
                    cursor.execute(
                        "INSERT INTO usuarios (nome, modulo) VALUES (?, ?)",
                        (form.nome.data, form.modulo.data),
                    )
                    session["user_id"] = cursor.lastrowid
                    session["nome"] = form.nome.data

        return redirect(url_for("desafio"))

    return render_template("index.html", form=form)


@app.route("/desafio", methods=["GET", "POST"])
def desafio():
    if "user_id" not in session:
        return redirect(url_for("index"))

    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()

        # Obter o total de questões
        cursor.execute("SELECT COUNT(*) FROM questoes")
        total_questoes = cursor.fetchone()[0]

        # Obter a próxima questão não respondida ou a última respondida incorretamente
        cursor.execute(
            """
            SELECT q.id, q.enunciado, q.dica, q.exemplo FROM questoes q
            LEFT JOIN progresso p ON q.id = p.questao_id AND p.usuario_id = ?
            WHERE p.id IS NULL OR (p.correto = 0 AND p.id = (
                SELECT MAX(id) FROM progresso WHERE usuario_id = ? AND questao_id = q.id
            ))
            ORDER BY q.id
            LIMIT 1
            """,
            (session["user_id"], session["user_id"]),
        )

        questao = cursor.fetchone()

        if not questao:
            return render_template("conclusao.html")

        # Obter tentativas anteriores para esta questão
        cursor.execute(
            """
            SELECT resposta_submetida, correto
            FROM progresso
            WHERE usuario_id = ? AND questao_id = ?
            ORDER BY id DESC
            """,
            (session["user_id"], questao["id"]),
        )
        tentativas_anteriores = cursor.fetchall()

        form = RespostaForm()
        if form.validate_on_submit():
            resposta_submetida = form.resposta.data
            cursor.execute(
                "SELECT resposta FROM questoes WHERE id = ?", (questao["id"],)
            )
            resposta_correta = cursor.fetchone()[0]

            correto = (
                resposta_submetida.lower().strip() == resposta_correta.lower().strip()
            )

            with conn:  # This automatically commits or rolls back
                cursor.execute(
                    """
                    INSERT INTO progresso (usuario_id, questao_id, resposta_submetida, correto)
                    VALUES (?, ?, ?, ?)
                    """,
                    (session["user_id"], questao["id"], resposta_submetida, correto),
                )

            if correto:
                flash("Correto! Avance para o próximo desafio.", "success")
            else:
                flash("Resposta incorreta. Tente novamente.", "error")

            return redirect(url_for("desafio"))

    return render_template(
        "desafio.html",
        questao=questao,
        form=form,
        total_questoes=total_questoes,
        tentativas_anteriores=tentativas_anteriores,
    )


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("nome", None)
    return redirect(url_for("index"))


@app.route("/download_csv")
def download_csv():
    if "user_id" not in session:
        flash("Você precisa estar logado para baixar o arquivo CSV.", "error")
        return redirect(url_for("index"))

    csv_path = os.path.join(app.root_path, "tech_company_data.csv")

    if not os.path.exists(csv_path):
        flash("O arquivo CSV não foi encontrado.", "error")
        return redirect(url_for("desafio"))

    return send_file(
        csv_path, as_attachment=True, download_name="tech_company_data.csv"
    )


@app.route("/conclusao")
def conclusao():
    if "user_id" not in session:
        return redirect(url_for("index"))

    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()

        # Obter todas as tentativas do usuário
        cursor.execute(
            """
            SELECT p.*, q.enunciado, q.id as questao_id
            FROM progresso p
            JOIN questoes q ON p.questao_id = q.id
            WHERE p.usuario_id = ?
            ORDER BY p.questao_id, p.timestamp
            """,
            (session["user_id"],),
        )

        tentativas = [dict(row) for row in cursor.fetchall()]

    # Converter timestamps para objetos datetime
    for tentativa in tentativas:
        tentativa["timestamp"] = datetime.strptime(
            tentativa["timestamp"], "%Y-%m-%d %H:%M:%S"
        )

    # Calcular estatísticas
    total_questoes = len(set(t["questao_id"] for t in tentativas))
    questoes_corretas = len(set(t["questao_id"] for t in tentativas if t["correto"]))
    total_tentativas = len(tentativas)

    if tentativas:
        tempo_total = (
            tentativas[-1]["timestamp"] - tentativas[0]["timestamp"]
        ).total_seconds() / 60  # em minutos
        tempo_medio_por_questao = (
            tempo_total / total_questoes if total_questoes > 0 else 0
        )
    else:
        tempo_total = 0
        tempo_medio_por_questao = 0

    questao_mais_tentativas = max(
        set(t["questao_id"] for t in tentativas),
        key=lambda q: sum(1 for t in tentativas if t["questao_id"] == q),
    )
    max_tentativas = sum(
        1 for t in tentativas if t["questao_id"] == questao_mais_tentativas
    )

    questoes_primeira_tentativa = [
        t["questao_id"]
        for t in tentativas
        if t["correto"]
        and sum(1 for tt in tentativas if tt["questao_id"] == t["questao_id"]) == 1
    ]

    # Questão que levou mais tempo
    tempos_questoes = {}
    for t in tentativas:
        if t["questao_id"] not in tempos_questoes:
            tempos_questoes[t["questao_id"]] = []
        tempos_questoes[t["questao_id"]].append(t["timestamp"])

    if tempos_questoes:
        questao_mais_tempo = max(
            tempos_questoes,
            key=lambda q: (
                max(tempos_questoes[q]) - min(tempos_questoes[q])
            ).total_seconds(),
        )
        tempo_max = (
            max(tempos_questoes[questao_mais_tempo])
            - min(tempos_questoes[questao_mais_tempo])
        ).total_seconds() / 60  # em minutos

        # Questão resolvida mais rápido
        questao_mais_rapida = min(
            tempos_questoes,
            key=lambda q: (
                max(tempos_questoes[q]) - min(tempos_questoes[q])
            ).total_seconds(),
        )
        tempo_min = (
            max(tempos_questoes[questao_mais_rapida])
            - min(tempos_questoes[questao_mais_rapida])
        ).total_seconds() / 60  # em minutos
    else:
        questao_mais_tempo = None
        tempo_max = 0
        questao_mais_rapida = None
        tempo_min = 0

    conn.close()

    return render_template(
        "conclusao.html",
        total_questoes=total_questoes,
        questoes_corretas=questoes_corretas,
        total_tentativas=total_tentativas,
        tempo_total=round(tempo_total, 2),
        tempo_medio_por_questao=round(tempo_medio_por_questao, 2),
        questao_mais_tentativas=questao_mais_tentativas,
        max_tentativas=max_tentativas,
        questoes_primeira_tentativa=questoes_primeira_tentativa,
        questao_mais_tempo=questao_mais_tempo,
        tempo_max=round(tempo_max, 2),
        questao_mais_rapida=questao_mais_rapida,
        tempo_min=round(tempo_min, 2),
    )


@app.route("/placar")
def placar():
    if "user_id" not in session:
        return redirect(url_for("index"))

    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()

        # Obter dados de progresso de todos os usuários
        cursor.execute("""
            SELECT u.id, u.nome, u.modulo, p.questao_id, p.correto, p.timestamp
            FROM usuarios u
            LEFT JOIN progresso p ON u.id = p.usuario_id
            ORDER BY u.id, p.questao_id, p.timestamp
        """)
        dados = cursor.fetchall()

        # Obter total de questões e dados das questões
        cursor.execute("SELECT COUNT(*) FROM questoes")
        total_questoes = cursor.fetchone()[0]
        cursor.execute("SELECT id, enunciado FROM questoes")
        questoes = {row["id"]: row["enunciado"] for row in cursor.fetchall()}

    # Processar dados
    usuarios = defaultdict(
        lambda: {"nome": "", "modulo": "", "questoes": defaultdict(list)}
    )
    for row in dados:
        user_id = row["id"]
        usuarios[user_id]["nome"] = row["nome"]
        usuarios[user_id]["modulo"] = row["modulo"]
        if row["questao_id"]:
            usuarios[user_id]["questoes"][row["questao_id"]].append(  # type: ignore
                {
                    "correto": row["correto"],
                    "timestamp": datetime.strptime(
                        row["timestamp"], "%Y-%m-%d %H:%M:%S"
                    ),
                }
            )

    # Calcular estatísticas
    estatisticas = []
    for user_id, user_data in usuarios.items():
        questoes_corretas = sum(
            1
            for q in user_data["questoes"].values()  # type: ignore
            if any(t["correto"] for t in q)
        )
        total_tentativas = sum(len(q) for q in user_data["questoes"].values())  # type: ignore
        tempo_total = sum(
            (
                max(q, key=itemgetter("timestamp"))["timestamp"]
                - min(q, key=itemgetter("timestamp"))["timestamp"]
            ).total_seconds()
            for q in user_data["questoes"].values()  # type: ignore
            if len(q) > 1
        )

        assertividade = (
            questoes_corretas / total_tentativas if total_tentativas > 0 else 0
        )
        tempo_medio_por_questao = (
            tempo_total / questoes_corretas if questoes_corretas > 0 else float("inf")
        )
        erro_medio = (
            (total_tentativas - questoes_corretas) / total_questoes
            if total_questoes > 0
            else 0
        )

        estatisticas.append(
            {
                "id": user_id,
                "nome": user_data["nome"],
                "modulo": user_data["modulo"],
                "questoes_corretas": questoes_corretas,
                "total_tentativas": total_tentativas,
                "assertividade": assertividade,
                "tempo_total": tempo_total,
                "tempo_medio_por_questao": tempo_medio_por_questao,
                "erro_medio": erro_medio,
            }
        )

    # Calcular estatísticas das questões
    estatisticas_questoes = []
    for questao_id, enunciado in questoes.items():
        tentativas = sum(
            len(user_data["questoes"].get(questao_id, []))  # type: ignore
            for user_data in usuarios.values()
        )
        acertos = sum(
            1
            for user_data in usuarios.values()
            if questao_id in user_data["questoes"]
            and any(t["correto"] for t in user_data["questoes"][questao_id])  # type: ignore
        )
        estatisticas_questoes.append(
            {
                "id": questao_id,
                "enunciado": enunciado,
                "tentativas": tentativas,
                "acertos": acertos,
                "dificuldade": tentativas / acertos if acertos > 0 else float("inf"),
            }
        )

    # Calcular rankings
    k = 10  # Número de top usuários/questões a serem exibidos
    top_assertividade = sorted(
        estatisticas, key=lambda x: x["assertividade"], reverse=True
    )[:k]
    top_tempo_medio = sorted(estatisticas, key=lambda x: x["tempo_medio_por_questao"])[
        :k
    ]
    top_eficiencia = sorted(estatisticas, key=lambda x: x["erro_medio"])[:k]
    top_dificeis = sorted(
        estatisticas_questoes, key=lambda x: x["dificuldade"], reverse=True
    )[:k]

    # Pódio de quem terminou as 50 questões
    podio = sorted(
        [user for user in estatisticas if user["questoes_corretas"] == total_questoes],
        key=lambda x: x["tempo_total"],
    )[:3]

    # Obter posição do usuário atual nos rankings
    user_id = session["user_id"]
    posicao_assertividade = next(
        (
            i + 1
            for i, e in enumerate(
                sorted(estatisticas, key=lambda x: x["assertividade"], reverse=True)
            )
            if e["id"] == user_id
        ),
        None,
    )
    posicao_tempo_medio = next(
        (
            i + 1
            for i, e in enumerate(
                sorted(estatisticas, key=lambda x: x["tempo_medio_por_questao"])
            )
            if e["id"] == user_id
        ),
        None,
    )
    posicao_eficiencia = next(
        (
            i + 1
            for i, e in enumerate(sorted(estatisticas, key=lambda x: x["erro_medio"]))
            if e["id"] == user_id
        ),
        None,
    )

    return render_template(
        "placar.html",
        top_assertividade=top_assertividade,
        top_tempo_medio=top_tempo_medio,
        top_eficiencia=top_eficiencia,
        top_dificeis=top_dificeis,
        podio=podio,
        posicao_assertividade=posicao_assertividade,
        posicao_tempo_medio=posicao_tempo_medio,
        posicao_eficiencia=posicao_eficiencia,
        total_usuarios=len(usuarios),
        total_questoes=total_questoes,
        media_assertividade=sum(e["assertividade"] for e in estatisticas)
        / len(estatisticas)
        if estatisticas
        else 0,
        media_tempo_por_questao=sum(
            e["tempo_medio_por_questao"]
            for e in estatisticas
            if e["tempo_medio_por_questao"] != float("inf")
        )
        / len([e for e in estatisticas if e["tempo_medio_por_questao"] != float("inf")])
        if estatisticas
        else 0,
        media_erro=sum(e["erro_medio"] for e in estatisticas) / len(estatisticas)
        if estatisticas
        else 0,
    )


if __name__ == "__main__":
    app.run(debug=True)
