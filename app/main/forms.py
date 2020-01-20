from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required, Length, DataRequired


class PostForm(FlaskForm):
    CATEGORIES=[('ART','ART'),('FINANCE','FINANCE'),('GAMING','GAMING'),('MUSIC','MUSIC')]
    