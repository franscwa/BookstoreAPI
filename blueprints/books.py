from flask import Blueprint, request
from werkzeug.exceptions import NotFound, BadRequest
from models.author import Author
from models.book import Book, book_schema, books_schema
from models.genre import Genre
from models.role import Roles
from http import HTTPStatus
from config.db import db
from config.authn import requires_authn
from config.authz import requires_roles

books_bp = Blueprint(name="books_bp", import_name=__name__, url_prefix="/api/v1/books")


@books_bp.get("/<isbn>")
def get_book(isbn):
    book = Book.query.get(isbn)
    if book is None:
        raise NotFound(f"Book [isbn={isbn}] not found.")
    return book_schema.jsonify(book), HTTPStatus.OK


@books_bp.post("")
@requires_authn
@requires_roles([Roles.ADMIN])
def create_book():
    book = book_schema.load(request.json)
    book.validate()
    if book.isbn in {b.isbn for b in Book.query.all()}:
        raise BadRequest(f"Book [isbn={book.isbn}] already exists.")
    if book.author_id not in {a.author_id for a in Author.query.all()}:
        raise NotFound(f"Author [author_id={book.author_id}] not found.")
    if book.genre_name not in {g.name for g in Genre.query.all()}:
        raise NotFound(f"Genre [genre_name={book.genre_name}] not found.")
    db.session.add(book)
    db.session.commit()
    return "", HTTPStatus.CREATED


@books_bp.get("/author/<author_id>")
def get_books_by_author(author_id):
    author = Author.query.get(author_id)
    if author is None:
        raise NotFound(f"Author [author_id={author_id}] not found.")
    return books_schema.jsonify(author.books), HTTPStatus.OK


@books_bp.get("/genre/<genre_name>")
def get_books_by_genre(genre_name):
    """
    Retrieve books by genre.
    """
    genre_books = Book.query.filter_by(genre_name=genre_name).all()
    if not genre_books:
        raise NotFound(f"No books found for genre {genre_name}.")
    return books_schema.jsonify(genre_books), HTTPStatus.OK


@books_bp.get("/top-sellers")
def get_top_selling_books():
    """
    Retrieve the top selling books.
    """
    top_selling_books = Book.query.order_by(Book.copies_sold.desc()).limit(10).all()
    if not top_selling_books:
        raise NotFound("No books found.")
    return books_schema.jsonify(top_selling_books), HTTPStatus.OK


@books_bp.put("/discount/<publisher>/<float:discount>")
def update_books_price(publisher, discount):
    """
    Update the price of books by a publisher.
    """
    books = Book.query.filter_by(publisher=publisher).all()
    if not books:
        raise NotFound(f"No books found for publisher {publisher}.")

    for book in books:
        original_price = book.price
        discounted_price = original_price * (1 - discount / 100)
        book.price = round(discounted_price, 2)
        db.session.commit()

    # Create a list of dictionaries with the original and discounted prices for each book
    price_changes = [
        {
            "discount_percent": discount,
            "book title": book.title,
            "original_price": round(original_price, 2),
            "discounted_price": book.price,
        }
        for book, original_price in zip(
            books, [b.price / (1 - discount / 100) for b in books]
        )
    ]
    return {"price_changes": price_changes}
