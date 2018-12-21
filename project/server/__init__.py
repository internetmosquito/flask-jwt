# project/server/__init__.py

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


bcrypt = Bcrypt()
db = SQLAlchemy()


def validate_token(token):
    """
    Just a utility method that makes sure provided token follows a 'Bearer token' spec
    :param token: A JWT token to be validated
    :return: The token itself, None if not valid
    :rtype: str
    """
    if token:
        # Token should be string with 'Bearer token'
        tokens = token.split(' ')
        # Make sure first token is Bearer
        if (len(tokens) == 2) and (tokens[0] == 'Bearer'):
            # Make sure token can be splitted by 3 using '.'
            elements = tokens[1].split('.')
            if len(elements) == 3:
                return tokens[1]
            else:
                raise Exception
        else:
            raise Exception
    else:
        return None


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_name)

    bcrypt.init_app(app)
    db.init_app(app)

    # Registering auth blueprint
    from project.server.auth.views import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
