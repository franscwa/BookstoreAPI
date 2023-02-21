from flask import Blueprint, request, jsonify, abort
from werkzeug.exceptions import NotFound
from models.book import Book, book_schema, books_schema
from models.author import Author
from http.client import OK, CREATED
from config.db import db
from sqlalchemy import select, desc


books_bp = Blueprint(name="books_bp", import_name=__name__, url_prefix="/api/v1/books")


@books_bp.get("/<isbn>")
def get_book(isbn):
    book = Book.query.get(isbn)
    if book is None:
        raise NotFound(f"Book [isbn={isbn}] not found.")
    return book_schema.jsonify(book), OK


@books_bp.post("")
def create_book():
    book = book_schema.load(request.json)
    book.validate()
    db.session.add(book)
    db.session.commit()
    # return "", CREATED
    return book_schema.jsonify(book), CREATED

@books_bp.get("/author/<author_id>")
def get_books_by_author(author_id):
    author = Author.query.get(author_id)
    if author is None:
        raise NotFound(f"Author [author_id={author_id}] not found.")
    return books_schema.jsonify(author.books), OK

@books_bp.get("/genre/<genre_name>")
def get_books_by_genre(genre_name):
    """
    Retrieve books by genre.
    """
    genre_books = Book.query.filter_by(genre_name=genre_name).all()
    if not genre_books:
        raise NotFound(f"No books found for genre {genre_name}.")
    return books_schema.jsonify(genre_books), OK

@books_bp.get("/top-sellers")
def get_top_selling_books():
    """
    Retrieve the top selling books.
    """
    top_selling_books = Book.query.order_by(Book.copies_sold.desc()).limit(10).all()
    if not top_selling_books:
        raise NotFound("No books found.")
    return books_schema.jsonify(top_selling_books), OK


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
        discounted_price = original_price * (1 - discount/100)
        book.price = round(discounted_price, 2)
        db.session.commit()

    # Create a list of dictionaries with the original and discounted prices for each book
    price_changes = [
       {"discount_percent": discount, "book title": book.title, "original_price": round(original_price, 2), "discounted_price": book.price}
       for book, original_price in zip(books, [b.price/(1-discount/100) for b in books])
    ]   
    return {"price_changes": price_changes}

@books_bp.get("/rating/<int:rating>")
def get_books_by_rating(rating):
    """
    Retrieve books by rating.
    """
    books = Book.query.filter(Book.rating >= rating).all()
    if not books:
        abort(404, f"No books found with rating >= {rating}.")
    
    return books_schema.jsonify(books), 200


#@books_bp.get("/rating/<int:rating>")
#def get_books_by_rating(rating):
#    """
#    Retrieve books by rating.
#    """
#    books = Book.query.join(Rating).filter(Rating.stars >= rating).all()
#    if not books:
#        abort(404, f"No books found with rating >= {rating}.")
    
#    return books_schema.jsonify(books), 200