from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class RegistroForm(FlaskForm):
    nome = StringField("Nome Completo", validators=[DataRequired()])
    modulo = SelectField(
        "Módulo",
        choices=[("II", "Módulo II"), ("IV", "Módulo IV"), ("Visitante", "Visitante")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Iniciar Desafio")


class RespostaForm(FlaskForm):
    resposta = StringField("Sua Resposta", validators=[DataRequired()])
    submit = SubmitField("Enviar")
