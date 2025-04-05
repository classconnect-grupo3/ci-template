from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .routes.ping import ping_bp
        app.register_blueprint(ping_bp)

    return app