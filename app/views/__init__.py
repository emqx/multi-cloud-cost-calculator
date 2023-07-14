from flask import Flask


def init_app(app: Flask):
    from .base import base_api_bp

    app.register_blueprint(base_api_bp, url_prefix='/api/v1')
