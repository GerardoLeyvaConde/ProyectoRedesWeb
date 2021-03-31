from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AñadirVertice(FlaskForm):
    id_vertice= StringField('id_vertice', validators=[DataRequired()])