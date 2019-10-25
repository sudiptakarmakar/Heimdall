import os


def get_env_var(name, strict=False, default=None):
    if strict:
        return os.environ[name]
    return os.environ.get(name, default)


def compose_database_conn_uri(
    strict=False,
    default_username=None,
    default_password=None,
    default_host=None,
    default_port=None,
    default_database=None,
):
    username = get_env_var("DATABASE_USERNAME", strict=strict, default=default_username)
    password = get_env_var("DATABASE_PASSWORD", strict=strict, default=default_password)
    host = get_env_var("DATABASE_HOST", strict=strict, default=default_host)
    port = get_env_var("DATABASE_PORT", strict=strict, default=default_port)
    database = get_env_var("DATABASE_NAME", strict=strict, default=default_database)
    if None in (username, password, host, port, database):
        raise ValueError("Values for username, password, host, port, database must not be empty")
    # [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
    return f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"


def get_database_conn_uri(strict=False):
    return get_env_var(
        "SQLALCHEMY_DATABASE_URI", strict=False
    ) or compose_database_conn_uri(strict=strict)


class Config:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = True
    FLASK_DEBUG = True
    SECRET_KEY = os.urandom(64)

    # Database
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
