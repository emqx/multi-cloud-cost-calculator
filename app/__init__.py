import os

from flask import Flask

flask_app = Flask(__name__, instance_relative_config=True)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_app(app=flask_app):
    views.init_app(app)
    return app
