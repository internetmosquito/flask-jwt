# project/server/tests/test_config.py

import os
import unittest

from flask import current_app
from flask_testing import TestCase

from project.server import create_app


class TestDevelopmentConfig(TestCase):

    def create_app(self):
        app_settings = os.getenv(
            'APP_SETTINGS',
            'project.server.config.DevelopmentConfig'
        )
        app = create_app(app_settings)
        return app

    def test_app_is_development(self):
        self.assertFalse(self.app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(self.app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            self.app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/flask_jwt_auth'
        )


class TestTestingConfig(TestCase):

    def create_app(self):
        app_settings = os.getenv(
            'APP_SETTINGS',
            'project.server.config.TestingConfig'
        )
        app = create_app(app_settings)
        return app

    def test_app_is_testing(self):
        self.assertFalse(self.app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(self.app.config['DEBUG'])
        self.assertTrue(
            self.app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/flask_jwt_auth_test'
        )


class TestProductionConfig(TestCase):

    def create_app(self):
        app_settings = os.getenv(
            'APP_SETTINGS',
            'project.server.config.ProductionConfig'
        )
        app = create_app(app_settings)
        return app

    def test_app_is_production(self):
        self.assertTrue(self.app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
