from config.common import Config, get_env_var, get_database_conn_uri


def get_prod_config():
    class ProdConfig(Config):
        """Set Flask configuration vars from .env file."""

        # General
        TESTING = False
        FLASK_DEBUG = False
        SECRET_KEY = get_env_var("SECRET_KEY", strict=True)

        # Database
        SQLALCHEMY_DATABASE_URI = get_database_conn_uri(strict=True)
        SQLALCHEMY_ECHO = False

    return ProdConfig
