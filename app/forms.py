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

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname already in use. Please choose another one.')
            return False
        return True
