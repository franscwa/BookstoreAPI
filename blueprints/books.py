from flask import Blueprint, request
from werkzeug.exceptions import NotFound
from models.book import Book, BookSchema
from http.client import OK, CREATED, NO_CONTENT, BAD_REQUEST
from config.db import db
from sqlalchemy import desc, select


books_bp = Blueprint(name="books", import_name=__name__, url_prefix="/api/v1/books")


book_schema = BookSchema()
books_schema = BookSchema(many=True)


@books_bp.get("")
def get_books():
    all_books = Book.query.all()
    return books_schema.jsonify(all_books)



#@books_bp.get("/<book_id>")
#def get_book(book_id):
#    book = Book.query.get(book_id)
#    if book is None:
#        raise NotFound(f"Book [book_id={book_id}] not found.")
#    return book_schema.jsonify(book), OK



@books_bp.get("/rating/<int:rating>")
def get_books_by_rating(rating):
    # Retrieve all books with a rating greater than or equal to the given rating
    books = Book.query.filter(Book.rating >= rating).all()
    # Return the books as a JSON response
    return books_schema.jsonify(books)


@books_bp.get("/top-sellers")
def get_top_sellers():
    # Select the top 10 books with the most sales
    top_books_query = select(
        Book, db.func.sum(Book.quantity_sold).label("total_sales")
    ).group_by(Book).order_by(desc("total_sales")).limit(10)
    top_books = [row[0] for row in db.session.execute(top_books_query)]

    return books_schema.jsonify(top_books)


@books_bp.get("/genre/<genre_name>")
def get_books_by_genre(genre_name):
    # Retrieve all books with the given genre
    books = Book.query.filter(Book.genre == genre_name).all()

    # Return the books as a JSON response
    return books_schema.jsonify(books)

@books_bp.put("/publisher-discount/<publisher_name>/<float:discount_percent>")
def update_publisher_discount(publisher_name, discount_percent):
    # Retrieve all books under the given publisher
    books = Book.query.filter(Book.publisher == publisher_name).all()

    # Update the price of each book by the given discount percent
    for book in books:
        original_price = round(book.price, 2)
        discounted_price = original_price * (1 - discount_percent/100)
        book.price = round(discounted_price, 2)

    # Commit the changes to the database
    db.session.commit()

    # Create a list of dictionaries with the original and discounted prices for each book
    price_changes = [
        {"title": book.title, "original_price": original_price, "discount_price": book.price}
        for book, original_price in zip(books, [b.price/(1-discount_percent/100) for b in books])
    ]
    # Return the list of price changes as a JSON response
    return {"price_changes": price_changes}


@books_bp.post("")
def create_book():
    new_book = book_schema.load(request.json)
    new_book.validate()
    db.session.add(new_book)
    db.session.commit()
    return book_schema.jsonify(new_book), CREATED


@books_bp.put("/<book_id>")
def update_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        raise NotFound(f"Book [book_id={book_id}] not found.")
    updated_book = book_schema.load(request.json)
    updated_book.validate()
    book.title, book.description, book.price = (
        updated_book.title,
        updated_book.description,
        updated_book.price,
    )
    db.session.commit()
    return book_schema.jsonify(book), OK


@books_bp.delete("/<book_id>")
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        raise NotFound(f"Book [book_id={book_id}] not found.")
    db.session.delete(book)
    db.session.commit()
    return "", NO_CONTENT
