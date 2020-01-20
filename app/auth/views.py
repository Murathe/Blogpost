from . import auth
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from ..models import User
from forms import SignupForm, LoginForm
from .. import db
from ..email import mail_message
import markdown2

@auth.route('/login', methods=['GET', 'POST'])
def login();
    login_form=LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.emial.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Wrong Username or Password')

    title = "Login"
    return render_template('auth/login.html', login_form = login_form, title = title)