""" app/__init__.py"""

from flask import Flask

from app.main import main
from app.auth import auth

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    return app