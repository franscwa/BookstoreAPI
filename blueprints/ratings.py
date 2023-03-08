from flask import Blueprint, request, jsonify
from models.rating import Rating, RatingSchema
from werkzeug.exceptions import NotFound
from http.client import OK, CREATED, NO_CONTENT, BAD_REQUEST
from config.db import db
from models.book import Book, BookSchema
from datetime import datetime


# cur = conn.cursor()

ratings_bp = Blueprint(name="ratings", import_name=__name__, url_prefix="/api/v1/book")
rating_schema = RatingSchema()
ratings_schema = RatingSchema(many=True)
book_schema = BookSchema()


@ratings_bp.get("/ratings")
def get_ratings():
    all_ratings = Rating.query.all()
    print(all_ratings)
    return ratings_schema.jsonify(all_ratings)


@ratings_bp.get("/<book_id>/ratings")
def get_ratings_by_book(book_id):
    rating_query = Rating.query.filter(Rating.books_id == book_id)
    if not rating_query:
        return jsonify(message="There are no ratings for this book.")
    return ratings_schema.jsonify(rating_query)


@ratings_bp.post("/<book_id>/ratings")
def create_rating(book_id):
    book = Book.query.get(book_id)
    if book is None:
        raise NotFound(f"Book [book_id={book_id}] not found.")
    res = request.json
    new_rating = Rating(rating=res["rating"], books_id=book_id, timestamp=datetime.now())
    new_rating.validate()
    db.session.add(new_rating)
    db.session.commit()
    return book_schema.jsonify(book)
    return rating_schema.jsonify(new_rating), CREATED


@ratings_bp.delete("/<book_id>/<rating_id>")
def delete_rating(book_id, rating_id):
    rating = Rating.query.get(rating_id)
    if rating is None:
        raise NotFound(f"Rating [rating_id={rating_id}] not found.")
    db.session.delete(rating)
    db.session.commit()
    rating_query = Rating.query.filter(Rating.books_id == book_id)
    return ratings_schema.jsonify(rating_query)



