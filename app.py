from flask import Flask
from db import db

from views import (
    main as main_blueprint,
    auth as auth_blueprint
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECURITY_USER_IDENTITY_ATTRIBUTES'] = 'login'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

app.register_blueprint(main_blueprint.main)
app.register_blueprint(auth_blueprint.auth)

if __name__ == '__main__':
    app.run()
