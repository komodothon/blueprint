"""app/auth/routes.py"""

from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from app.forms import RegisterForm, LoginForm
from app import db, bcrypt
from app.models import User

from . import auth



@auth.route("/register", methods=["GET", "POST"])
def register():
    """User Register"""
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        new_user = User(username=username, email=email, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash("New User registered successfully!", "info")

        except Exception as e:
            flash("An error occurred during registering new user.", "danger")
            db.session.rollback()
            return redirect(url_for("auth.register"))


        return redirect(url_for("main.home"))

    return render_template("register.html", form=register_form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    """User login"""

    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user = db.session.query(User).filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("User successfully logged IN", "info")
            return redirect(url_for("main.home"))

    return render_template("login.html", form=login_form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("User successfully logged OUT", "info")
    return redirect(url_for("main.home"))