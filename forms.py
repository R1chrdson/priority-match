from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Optional
from db import User


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Увійти')

    def validate(self):
        initial_validation = super().validate()
        if not initial_validation:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Користувача з таким логіном не існує!')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Невірний пароль!')
            return False

        return True


class SignUpForm(FlaskForm):
    username = StringField(validators=[DataRequired(),
                                       Length(min=3, max=15, message='Довжина логіну від 3х до 15ти символів!')])
    password = PasswordField(validators=[DataRequired(),
                                         Length(min=6, max=20, message='Довжина пароля від 6ти до 20ти символів!')])
    confirm = PasswordField(validators=[DataRequired(),
                                        EqualTo('password', message='Паролі не співпадають!')])
    submit = SubmitField('Зареєструватись')

    def validate(self):
        initial_validation = super().validate()
        if not initial_validation:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Користувач з таким логіном вже існує!")
            return False

        return True
