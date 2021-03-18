from flask import Flask
from login_manager import login_manager
from flask_assets import Environment, Bundle
import os.path

app = Flask(__name__, static_folder=os.path.abspath('static'))
app.config['SECRET_KEY'] = 'SecretKey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECURITY_USER_IDENTITY_ATTRIBUTES'] = 'login'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

css = Bundle('src/css/main.css', filters='postcss', output='static/css/main.css')
assets = Environment(app)
assets.register('css', css)

login_manager.init_app(app)
login_manager.login_view = '/auth/login'
login_manager.login_message = 'Будь ласка авторизуйтесь!'

from views import (
    main as main_blueprint,
    auth as auth_blueprint
)

app.register_blueprint(main_blueprint.main)
app.register_blueprint(auth_blueprint.auth)


if __name__ == '__main__':
    app.run()
