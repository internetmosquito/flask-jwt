# project/server/tests/base.py
import os

from flask_testing import TestCase

from project.server import create_app, db


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app_settings = os.getenv(
            'APP_SETTINGS',
            'project.server.config.TestingConfig'
        )
        app = create_app(app_settings)
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
