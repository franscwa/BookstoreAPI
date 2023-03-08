from flask import Flask, jsonify
from blueprints.books_bp import books_bp
from config.app_config import APP_CONFIG
from config.db import db
from config.ma import ma
from werkzeug.exceptions import HTTPException
from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR
from dotenv import load_dotenv
from models.book import Book

app = Flask(__name__)
app.config.from_mapping(APP_CONFIG)

ma.init_app(app)
db.init_app(app)

app.register_blueprint(books_bp)


@app.errorhandler(Exception)
def default_error(e):
    if isinstance(e, HTTPException):
        return jsonify(error=e.description), e.code
    elif isinstance(e, AssertionError):
        return jsonify(error=str(e)), BAD_REQUEST
    return jsonify(error=str(e)), INTERNAL_SERVER_ERROR


def init_db():
    """Initialize the database."""
    with app.app_context():
        db.drop_all()
        db.create_all()
    print("database initialized")


def seed_db():
    """Seed the database."""
    with app.app_context():
        book1 = Book(title="The Hobbit", description="A great book", price=10.99)
        book2 = Book(title="The Silmarillion", description="A great book", price=11.99)
        book3 = Book(
            title="The Fellowship of the Ring", description="A great book", price=12.99
        )
        book4 = Book(title="The Two Towers", description="A great book", price=13.99)
        book5 = Book(
            title="The Return of the King", description="A great book", price=15.99
        )
        books = [book1, book2, book3, book4, book5]
        db.session.add_all(books)
        db.session.commit()
    print("database seeded")


if __name__ == "__main__":
    init_db()
    seed_db()
    app.run(port=app.config["PORT"])
