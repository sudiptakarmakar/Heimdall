from config import Config
from flask import Flask


def create_app(*args, **kwargs):

    app = Flask(__name__)
    app.config.from_object(getattr(Config, kwargs["env"]))

    from heimdall import models, routes
    models.init_app(app)
    routes.init_app(app)

    return app
