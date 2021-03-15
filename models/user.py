from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from app import login_manager
from flask import redirect


class User(UserMixin, db.Model):
    _tablename = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password_hash = db.Column(db.String(80))

    def __repr__(self):
        return f'<User({self.username!r})>'

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
