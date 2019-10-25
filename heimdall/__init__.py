from config import Config
from flask import Flask


def create_app(*args, **kwargs):

    app = Flask(__name__)
    app_config_callable = getattr(Config, kwargs["env"])
    app.config.from_object(app_config_callable())

    from heimdall import models, routes

    models.init_app(app)
    routes.init_app(app)

    return app
