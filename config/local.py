from config.common import Config


def get_local_config():

    class LocalConfig(Config):
        """Set Flask configuration vars from .env file."""

        # General
        TESTING = True
        FLASK_DEBUG = True

        # Database
        SQLALCHEMY_ECHO = True

    return LocalConfig
