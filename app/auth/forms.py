from flask_wtf import FlaskForm
from wtfforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidateError 

class SignupForm(FlaskForm):
    