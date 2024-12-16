from app import db
from flask_login import UserMixin
from datetime import datetime

# User model

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)

    posts = db.relationship("Post", backref="author")

    def __repr__(self):
        return f"<User(id: {self.id}, username:{self.username}, email:{self.email})>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Post(id: {self.id}, title: {self.title}, date: {self.date})"
    