from flask import Blueprint, request, jsonify
from models.rating import Rating, rating_schema, ratings_schema
from werkzeug.exceptions import NotFound
from http.client import OK, CREATED, NO_CONTENT, BAD_REQUEST
from config.db import db
from models.book import Book, book_schema, books_schema
from datetime import datetime

ratings_bp = Blueprint(name="ratings", import_name=__name__, url_prefix="/api/v1/book")


@ratings_bp.get("/ratings")
def get_ratings():
    all_ratings = Rating.query.all()
    print(all_ratings)
    return ratings_schema.jsonify(all_ratings)


@ratings_bp.get("/<isbn>/ratings")
def get_ratings_by_book(isbn):
    rating_query = Rating.query.filter(Rating.isbn == isbn)
    if not rating_query:
        return jsonify(message="There are no ratings for this book.")
    return ratings_schema.jsonify(rating_query)


@ratings_bp.get("/<isbn>/rating")
def get_avg_rating(isbn):
    rating_query = Rating.query.filter(Rating.isbn == isbn)
    book = Book.query.get(isbn)
    if not book:
        return jsonify(message="There is no book with that isbn")
    if not rating_query:
        return jsonify(message="There are no ratings for this book.")
    sum = 0
    count = 0
    for r in rating_query:
        count += 1
        sum += r.rating
    avg = sum / count
    print(sum, count, round(avg, 2))
    book.avg_rating = round(avg, 2)
    # return jsonify(average=f"{avg:.2}")
    # return ratings_schema.jsonify(rating_query)
    return book_schema.jsonify(book)


@ratings_bp.post("/<isbn>/ratings")
def create_rating(isbn):
    sBook = Book.query.get(isbn)
    if sBook is None:
        raise NotFound(f"Book [book={isbn}] not found.")
    res = request.json
    new_rating = Rating(
        rating=res["rating"],
        isbn=isbn,
        book=sBook,
        user_id=res["user_id"],
        timestamp=datetime.now(),
    )
    new_rating.validate()
    db.session.add(new_rating)
    db.session.commit()
    return book_schema.jsonify(sBook), CREATED


@ratings_bp.delete("/<isbn>/<rating_id>")
def delete_rating(isbn, rating_id):
    rating = Rating.query.get(rating_id)
    print(rating)
    if rating is None:
        raise NotFound(f"Rating [rating_id={rating_id}] not found.")
    db.session.delete(rating)
    db.session.commit()
    rating_query = Rating.query.filter(Rating.isbn == isbn)
    return ratings_schema.jsonify(rating_query)
