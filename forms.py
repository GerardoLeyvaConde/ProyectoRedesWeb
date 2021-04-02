from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AñadirVertice(FlaskForm):
    id_vertice= StringField('id_vertice', validators=[DataRequired()])

class AgregarArista(FlaskForm):
    id_a1= StringField('id_a1', validators=[DataRequired()])
    id_a2= StringField('id_a2', validators=[DataRequired()])
