import os
from dotenv import load_dotenv

load_dotenv()

APP_CONFIG = {
    "PORT": os.getenv("PORT"),
    "DEBUG": os.getenv("DEBUG"),
    "TESTING": os.getenv("TESTING"),
    "FLASK_ENV": os.getenv("FLASK_ENV"),
    "FLASK_APP": os.getenv("FLASK_APP"),
    "SQLALCHEMY_TRACK_MODIFICATIONS": os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS"),
    "SQLALCHEMY_DATABASE_URI": os.getenv("SQLALCHEMY_DATABASE_URI"),
}
