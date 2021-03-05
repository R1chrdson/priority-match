from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Optional


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired(),
                           Length(min=3, max=15, message='Довжина логіну від 3х до 15ти символів!')])
    password = PasswordField(validators=[DataRequired(),
                             Length(min=6,
                                    message='Вкажіть пароль з довжиною пароля мінімум 6 символів!')])
    submit = SubmitField('Увійти')
