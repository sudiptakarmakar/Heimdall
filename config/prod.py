import os


class Config:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = False
    FLASK_DEBUG = False
    SECRET_KEY = os.environ["SECRET_KEY"]

    # Database
    # [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
    # username = os.environ["DATABASE_USERNAME"]
    # password = os.environ["DATABASE_PASSWORD"]
    # host = os.environ["DATABASE_HOST"]
    # port = os.environ["DATABASE_PORT"]
    # database = os.environ["DATABASE_NAME"]
    # database_connection_uri = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
