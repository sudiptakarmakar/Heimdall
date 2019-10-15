import os
import uuid


class Config:

    # General
    TESTING = os.environ.get("TESTING") or True
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG") or True
    SECRET_KEY = os.environ.get('SECRET_KEY') or str(uuid.uuid4()).lower()

    # Database
    # [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
    username = os.environ.get('DATABASE_USERNAME') or "nobody"
    password = os.environ.get('DATABASE_PASSWORD') or "**********"
    host = os.environ.get('DATABASE_HOST') or "localhost"
    port = os.environ.get('DATABASE_PORT') or 5432
    database = os.environ.get('DATABASE_NAME') or "heimdalldb"
    database_connection_uri = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or database_connection_uri
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO") or True
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") or False
