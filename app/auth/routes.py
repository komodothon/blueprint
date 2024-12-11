"""app/auth/routes.py"""

from flask import render_template

from . import auth

@auth.route("/login")
def login():
    return render_template("login.html",)

@auth.route("/register")
def register():
    return render_template("register.html")

@auth.route("/logout")
def logout():
    return "<h5>User Logged Out</h5>"