from flask import render_template, redirect, flash, url_for

from app.models import User

from . import bp 
from app.forms import SignUpForm

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
                last_name=form.last_name.data,
                password=form.password.data
            )
            u.commit()
            flash(f"{input_email} successfully registered!")
            return redirect(url_for("main.home"))
        else:
            flash(f"{input_email} already registered. Try again.")
    return render_template(
        'signup.jinja',
        title="PokeFavorites: SignUp",
        form=form
    )