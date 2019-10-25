from config.common import Config, get_database_conn_uri


def get_dev_config():

    class DevConfig(Config):

        # General
        TESTING = True
        FLASK_DEBUG = False

        # Database
        SQLALCHEMY_DATABASE_URI = get_database_conn_uri(strict=True)
        SQLALCHEMY_ECHO = False

    return DevConfig
