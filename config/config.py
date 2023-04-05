import os
from dotenv import load_dotenv


def load_config():
    load_dotenv()
    config = {}
    keys = [
        "FLASK_RUN_PORT",
        "FLASK_APP",
        "FLASK_DEBUG",
        "SECRET_KEY",
        "SQLALCHEMY_TRACK_MODIFICATIONS",
        "SQLALCHEMY_DATABASE_URI",
    ]
    for key in keys:
        val = os.getenv(key)
        if val is None:
            raise ValueError(f"Must set environment variable: {key}")
        config[key] = val
    return config


app_config = load_config()
