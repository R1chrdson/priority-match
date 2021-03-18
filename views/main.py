from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from forms import EditProfileForm
import os.path

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    print(current_user)
    form = EditProfileForm()
    avatar_src = url_for('static', filename=f'user-avatar/{current_user.id}.svg')
    if not os.path.isfile(avatar_src):
        avatar_src = url_for('static', filename=f'user-avatar/default.svg')

    return render_template('profile.html', avatar_src=avatar_src, form=form, user=current_user)
