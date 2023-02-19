import os
from dotenv import load_dotenv

load_dotenv()

APP_CONFIG = {}

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
        raise ValueError(f"Missing environment variable: {key}")
    APP_CONFIG[key] = val
