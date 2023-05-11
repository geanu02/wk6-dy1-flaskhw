from flask import render_template, redirect, flash, url_for
from flask_login import login_user
from app.models import User

from . import bp
from app.forms import SignUpForm, SigninForm


@bp.route('signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        input_email = form.email.data
        email_check = User.query.filter_by(email=input_email).first()
        if not email_check:
            u = User(
                email=input_email,
                first_name=form.first_name.data,
                last_name=form.last_name.data
            )
            u.password = u.hash_password(form.password.data)
            u.commit()
            flash(f"{input_email} successfully registered!", "success")
            return redirect(url_for("main.home"))
        else:
            flash(f"{input_email} already registered. Try again.", "warning")
    return render_template(
        'signup.jinja',
        title="PokeFavorites: SignUp",
        form=form
    )


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            flash(f"{form.email.data} signed in.", "success")
            login_user(user)
            return redirect(url_for("main.home"))
        else:
            flash(
                f"{form.email.data} does not exist or incorrect password.", "warning")
    return render_template(
        'signin.jinja',
        title="PokeFavorites: Signin",
        form=form
    )
