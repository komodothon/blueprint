""" app/__init__.py"""

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

# flask_login
login_manager = LoginManager()

from app.models import User
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

def create_app():
    app = Flask(__name__)

    # app configurations
    app.config['SECRET_KEY'] = 'app_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posts.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialise
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)


    # Flask-Login setup
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please login to access this page.'
    login_manager.login_message_category = 'info'

    from app.main import main
    from app.auth import auth

    # Register blueprints
    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    return app