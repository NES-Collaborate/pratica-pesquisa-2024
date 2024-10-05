import sqlite3

import numpy as np
import pandas as pd

# Conectar ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect("ctf_pandas.db")
cursor = conn.cursor()

# Executar os comandos SQL para criar as tabelas
with open("schema.sql", "r") as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)


df = pd.read_csv("tech_company_data.csv")


questoes = [
    {
        "enunciado": "Quantas entradas tem o csv?",
        "dica": "Shape??",
        "resposta": df.shape[0],
    },
    {
        "enunciado": "Quantas colunas tem o csv?",
        "dica": "Shape??",
        "resposta": df.shape[1],
    },
    {
        "enunciado": "Insira as colunas separadas por vírgula e espaço.",
        "exemplo": "Coluna 1, Coluna 2, Coluna 3",
        "dica": "`.join` is your friend!",
        "resposta": ", ".join(df.columns),
    },
    {
        "enunciado": "Qual é a média de idade dos funcionários? [Arredondada para 2 casas decimais]",
        "dica": "Meaaanwn~",
        "resposta": round(df["Idade"].mean(), 2),
    },
    {
        "enunciado": "Quantos funcionários trabalham no departamento de TI?",
        "dica": "len ou values_counts",
        "resposta": len(df[df["Departamento"] == "TI"]),
    },
    {
        "enunciado": "Qual é o nome do funcionário mais velho?",
        "dica": "ID Max",
        "resposta": df.loc[df["Idade"].idxmax(), "Nome"],
    },
    {
        "enunciado": "O nome do funcionário mais velho está bagunçado né? Bora consertar? Qual é o nome real?",
        "dica": "Give your jumps!",
        "resposta": df.loc[df["Idade"].idxmin(), "Nome"],
    },
    {
        "enunciado": "Quantos funcionários têm mais de 5 anos na empresa?",
        "dica": "Use uma condição booleana e sum().",
        "resposta": str((df["AnosNaEmpresa"] > 5).sum()),
    },
    {
        "enunciado": "Qual é a média de projetos completos para funcionários Sênior?",
        "dica": "Duas casas decimais...",
        "resposta": str(
            round(df[df["Cargo"] == "Sênior"]["ProjetosCompletos"].mean(), 2)
        ),
    },
    {
        "enunciado": "Quem tem a maior avaliação de desempenho?",
        "dica": "idmax; Nome real.",
        "resposta": df.loc[df["AvaliacaoDesempenho"].idxmax(), "Nome"],
    },
    {
        "enunciado": "Qual é o total de horas extras trabalhadas por todos os funcionários?",
        "dica": "Será que todo mundo é número mesmo?",
        "resposta": str(df["HorasExtras"].str.replace("h", "").astype(int).sum()),
    },
    {
        "enunciado": "Quantos funcionários foram contratados em 2022?",
        "dica": "dt.year == 2022",
        "resposta": str(
            df[pd.to_datetime(df["DataContratacao"]).dt.year == 2022].shape[0]
        ),
    },
    {
        "enunciado": "Qual é o salário médio no departamento de Marketing?",
        "dica": "Duas casas decimais...; Será que todo mundo é número mesmo?",
        "resposta": f"R$ {df[df['Departamento'] == 'Marketing']['Salario'].str.replace('R$ ', '').astype(float).mean():.2f}",
    },
    {
        "enunciado": "Quem tem o maior número de certificações?",
        "dica": "Já falei duas vezes.",
        "resposta": df.loc[df["Certificacoes"].idxmax(), "Nome"],
    },
    {
        "enunciado": "Qual é a média de linguagens dominadas por funcionários Pleno?",
        "dica": "Filtre para Pleno e use mean() em 'LinguagensDominadas'.",
        "resposta": str(
            round(df[df["Cargo"] == "Pleno"]["LinguagensDominadas"].mean())
        ),
    },
    {
        "enunciado": "Qual é o total de bônus anuais a serem pagos (excluindo valores nulos)?",
        "dica": "DROP NAAAAAAA",
        "exemplo": "R$ 10000.00",
        "resposta": f"R$ {df['BonusAnual'].dropna().sum():.2f}",
    },
    {
        "enunciado": "Quantos funcionários têm mais de 25 dias de férias?",
        "dica": "Use uma condição booleana e sum().",
        "resposta": str((df["DiasFerias"] > 25).sum()),
    },
    {
        "enunciado": "Qual é a média de treinamentos realizados por funcionários do departamento de RH?",
        "dica": "Não precisa arredondar...",
        "resposta": str(
            df[df["Departamento"] == "RH"]["TreinamentosRealizados"].mean()
        ),
    },
    {
        "enunciado": "Quem tem o maior score de inovação?",
        "dica": "idxmax; Nome Real.",
        "resposta": df.loc[df["ScoreInovacao"].idxmax(), "Nome"],
    },
    {
        "enunciado": "Qual é a participação nos lucros média (em percentual)?",
        "dica": "Duas casa decimais :D",
        "resposta": f"{df['ParticipacaoLucros'].str.rstrip('%').astype(float).mean():.2f}%",
    },
    {
        "enunciado": "Quantos funcionários atingiram todas as metas trimestrais?",
        "dica": "Quantos trimestres tem em um ano mesmo?",
        "resposta": str((df["MetasTrimestrais"] == 4).sum()),
    },
    {
        "enunciado": "Qual é o email do funcionário mais recentemente contratado?",
        "dica": "sort values",
        "resposta": df.sort_values("DataContratacao", ascending=False).iloc[0]["Email"],
    },
    {
        "enunciado": "Quantos funcionários têm nomes que começam com a letra 'M'?",
        "dica": "Use str.startswith() e sum().",
        "resposta": str(df["Nome"].str.startswith("M").sum()),
    },
    {
        "enunciado": "Qual é a média de idade dos gerentes?",
        "dica": "Duas casas decimais...",
        "resposta": str(round(df[df["Cargo"] == "Gerente"]["Idade"].mean(), 2)),
    },
    {
        "enunciado": "Quem tem o menor salário entre os funcionários Sênior?",
        "dica": "Filtre para Sênior, ordene por salário e pegue o primeiro nome.",
        "resposta": df[df["Cargo"] == "Sênior"].sort_values("Salario").iloc[0]["Nome"],
    },
    {
        "enunciado": "Qual é o total de projetos completos no departamento de Desenvolvimento?",
        "dica": "Filtre para Desenvolvimento e some 'ProjetosCompletos'.",
        "resposta": str(
            df[df["Departamento"] == "Desenvolvimento"]["ProjetosCompletos"].sum()
        ),
    },
    {
        "enunciado": "Quantos funcionários têm um score de inovação acima de 7?",
        "dica": "Use uma condição booleana e sum().",
        "resposta": str((df["ScoreInovacao"] > 7).sum()),
    },
    {
        "enunciado": "Qual é a média de anos na empresa para funcionários com mais de 40 anos?",
        "resposta": str(round(df[df["Idade"] > 40]["AnosNaEmpresa"].mean(), 2)),
    },
    {
        "enunciado": "Quem tem o maior bônus anual?",
        "resposta": df.loc[df["BonusAnual"].dropna().idxmax(), "Nome"],
    },
    {
        "enunciado": "Qual é o departamento com o maior número de funcionários?",
        "resposta": df["Departamento"].value_counts().index[0],
    },
    {
        "enunciado": "Quantos funcionários têm pelo menos 3 certificações?",
        "dica": "PELO MENOS 3 CERTIFICACOES",
        "resposta": str((df["Certificacoes"] >= 3).sum()),
    },
    {
        "enunciado": "Qual é a média de horas extras dos funcionários Júnior?",
        "dica": "Todas as horas estão em número mesmo?; Duas casas decimais...",
        "resposta": f"{df[df['Cargo'] == 'Júnior']['HorasExtras'].str.replace('h', '').astype(int).mean():.2f}h",
    },
    {
        "enunciado": "Quem tem o menor número de dias de férias?",
        "dica": "se tem max, deve ter min né?",
        "resposta": df.loc[df["DiasFerias"].idxmin(), "Nome"],
    },
    {
        "enunciado": "Qual é a soma total de metas trimestrais atingidas por todos os funcionários?",
        "dica": "Use sum() na coluna 'MetasTrimestrais'.",
        "resposta": str(df["MetasTrimestrais"].sum()),
    },
    {
        "enunciado": "Quantos funcionários têm um email que termina com '@gmail.com'?",
        "dica": "Use str.endswith() e sum().",
        "resposta": str(df["Email"].str.endswith("@gmail.com").sum()),
    },
    {
        "enunciado": "Qual é a média de avaliação de desempenho para funcionários com mais de 10 anos na empresa?",
        "dica": "Duas casas decimais...",
        "resposta": str(
            round(df[df["AnosNaEmpresa"] > 10]["AvaliacaoDesempenho"].mean(), 2)
        ),
    },
    {
        "enunciado": "Quem é o funcionário mais jovem no departamento de Vendas?",
        "dica": "Filtre para Vendas, ordene por idade e pegue o último nome.",
        "resposta": df[df["Departamento"] == "Vendas"]
        .sort_values("Idade")
        .iloc[0]["Nome"]
        .split("|")[0][::-1],
    },
    {
        "enunciado": "Qual é o total de linguagens dominadas por todos os funcionários?",
        "dica": "Ta ficando chato isso de questão fácil.",
        "resposta": str(df["LinguagensDominadas"].sum()),
    },
    {
        "enunciado": "Quantos funcionários são do departamento de TI e têm mais de 5 anos de experiência?",
        "dica": "Use filtragem múltipla com &",
        "resposta": str(
            len(df[(df["Departamento"] == "TI") & (df["AnosNaEmpresa"] > 5)])
        ),
    },
    {
        "enunciado": "Qual é a média de salário dos funcionários que são Sênior ou têm mais de 10 anos na empresa?",
        "dica": "Use | para condições OR e lembre-se de tratar o formato do salário",
        "resposta": f"R$ {df[(df['Cargo'] == 'Sênior') | (df['AnosNaEmpresa'] > 10)]['Salario'].str.replace('R$ ', '').astype(float).mean():.2f}",
    },
    {
        "enunciado": "Qual é o departamento com a maior média de avaliação de desempenho?",
        "dica": "Use groupby e aggregate",
        "resposta": df.groupby("Departamento")["AvaliacaoDesempenho"].mean().idxmax(),
    },
    {
        "enunciado": "Qual é a soma total de projetos completos por cargo?",
        "dica": "Use groupby e sum",
        "resposta": str(dict(df.groupby("Cargo")["ProjetosCompletos"].sum())),
    },
    {
        "enunciado": "Qual é a mediana de idade no dataset?",
        "dica": "Use o método describe()",
        "resposta": str(df["Idade"].describe()["50%"]),
    },
    {
        "enunciado": "Quantas colunas numéricas existem no dataset?",
        "dica": "Use o método info() e verifique os tipos de dados",
        "resposta": str(df.select_dtypes(include=[np.number]).shape[1]),
    },
    {
        "enunciado": "Quantos valores NaN existem na coluna 'Salario'?",
        "dica": "Use isna() ou isnull()",
        "resposta": str(df["Salario"].isna().sum()),
    },
    {
        "enunciado": "Qual é o total de valores NaN em todo o DataFrame?",
        "dica": "Use isna() em todo o DataFrame",
        "resposta": str(df.isna().sum().sum()),
    },
    {
        "enunciado": "Qual coluna tem o maior número de valores NaN?",
        "dica": "Use isna().sum() e idxmax()",
        "resposta": df.isna().sum().idxmax(),
    },
    {
        "enunciado": "Qual é a diferença média entre o salário e o bônus anual?",
        "dica": "Lembre-se de converter o salário para numérico",
        "resposta": f"R$ {(df['Salario'].str.replace('R$ ', '').astype(float) - df['BonusAnual']).mean():.2f}",
    },
    {
        "enunciado": "Qual é o aumento percentual médio do salário em relação ao bônus anual?",
        "dica": "Use a fórmula: (salário + bônus) / salário - 1",
        "resposta": f"{((df['Salario'].str.replace('R$ ', '').astype(float) + df['BonusAnual']) / df['Salario'].str.replace('R$ ', '').astype(float) - 1).mean() * 100:.2f}%",
    },
    {
        "enunciado": "Quem tem o maior aumento absoluto de salário considerando o bônus anual?",
        "dica": "Calcule o aumento para cada funcionário e use idxmax()",
        "resposta": df.loc[
            (
                df["Salario"].str.replace("R$ ", "").astype(float)
                + df["BonusAnual"]
                - df["Salario"].str.replace("R$ ", "").astype(float)
            ).idxmax(),
            "Nome",
        ],
    },
]

# Inserir as questões no banco de dados
for questao in questoes:
    cursor.execute(
        """
    INSERT INTO questoes (enunciado, dica, exemplo, resposta)
    VALUES (?, ?, ?, ?)
    """,
        (
            questao["enunciado"],
            questao.get("dica"),
            questao.get("exemplo"),
            questao["resposta"],
        ),
    )

# Commit das mudanças e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados inicializado e questões inseridas com sucesso!")
