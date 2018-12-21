# project/server/__init__.py

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_name)

    bcrypt.init_app(app)
    db.init_app(app)

    # Registering auth blueprint
    from project.server.auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
