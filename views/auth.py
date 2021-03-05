from flask import Blueprint, render_template, request, flash, redirect
from forms import LoginForm
from flask_login import login_required
from db import User

auth = Blueprint('auth', __name__)

#
# @auth.route('/login', methods=('GET', 'POST'))
# def login():
#     form = LoginForm(request.form)
#     if request.method == 'POST' and :
#         redirect('/profile')
#
#     for field, errors in form.errors.items():
#         for error in errors:
#             flash(error)
#     return render_template('login.html', form=form)


@auth.route('/signup')
def signup():
    return


@auth.route('/logout')
@login_required
def logout():
    return 'Logout'