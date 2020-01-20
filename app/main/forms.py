from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required, Length, DataRequired


class PostForm(FlaskForm):
    CATEGORIES= [('ART','ART'),('FINANCE','FINANCE'),('GAMING','GAMING'),('MUSIC','MUSIC')]
    category = SelectField('CATEGORIES',choices=CATEGORIES)
    titles = StringField('TITLE', validators=[DataRequired()])
    post = TextAreaField('BLOG', VALIDATORS=[Required()])
    submit = SubmitField('Publish')

class CommentForm(FlaskForm):
    comment = TextAreaField('')
    submit = SubmitField('Submit')