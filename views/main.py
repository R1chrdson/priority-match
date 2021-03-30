from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from forms import EditProfileForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    print(current_user)
    form = EditProfileForm()
    return render_template('profile.html', form=form, user=current_user)
