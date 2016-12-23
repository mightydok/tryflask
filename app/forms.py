# encoding: utf-8

from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, StringField
from wtforms.validators import Required, Length, DataRequired

class LoginForm(FlaskForm):
    openid = TextField('openid', validators= [Required()])
    remember_me = BooleanField('remember_me', default=False)

class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
