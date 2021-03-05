from flask import Blueprint, render_template, request, flash, redirect
from forms import LoginForm, SignUpForm
from flask_login import login_required, login_user
from db import db, User

auth = Blueprint('auth', __name__)


@auth.route('/auth/<auth_type>', methods=('GET', 'POST'))
def authentication(auth_type):
    form = LoginForm(request.form) if auth_type == 'login' else SignUpForm(request.form)
    template = f'{auth_type}.html'

    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data)
        if auth_type == 'signup':
            db.session.add(user)
            db.session.commit()
        if auth_type =='login':
            login_user(user)
            print(user.is_authenticated)
        return redirect('/profile')

    for field, errors in form.errors.items():
        for error in errors:
            flash(error)
    return render_template(template, form=form)

@auth.route('/logout')
@login_required
def logout():
    return 'Logout'
