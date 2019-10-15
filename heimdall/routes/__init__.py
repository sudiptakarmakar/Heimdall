from flask import Flask, jsonify
from heimdall.routes.api import bp as api_bp
from heimdall.routes.home import bp as home_bp
from heimdall.routes.users import bp as users_bp


def init_app(app: Flask):
    app.register_blueprint(home_bp)
    app.register_blueprint(api_bp, url_prefix="/api/v1/")
    app.register_blueprint(users_bp, url_prefix="/users/")

    @app.errorhandler(404)
    @app.errorhandler(405)
    def handle_error(error):
        return jsonify(error=str(error))
