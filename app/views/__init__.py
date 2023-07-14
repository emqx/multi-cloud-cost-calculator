def init_app(app: Flask):
    from .base import base_bp

    app.register_blueprint(base_bp, url_prefix='/api/v1')
