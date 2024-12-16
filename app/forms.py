from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, TextAreaField, DateTimeLocalField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    email = EmailField("Email:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password:", validators=[DataRequired(), EqualTo(fieldname="password", message="Passwords must match")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("Login")

class CreatePostForm(FlaskForm):
    title = StringField("Title:", validators=[DataRequired()])
    content = TextAreaField("Content:", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
