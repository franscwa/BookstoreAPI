from datetime import datetime
from flask import Blueprint, request, jsonify
from models.rating import Rating, RatingSchema
from models.book import Book
from models.user import User
from config.db import db

rating_bp = Blueprint('rating_bp', __name__, url_prefix='/api/v1/ratings')

@rating_bp.route('', methods=['POST'])
def create_rating():
    # Parse request data
    data = request.json
    rating_value = data.get('rating')
    user_id = data.get('user_id')
    book_isbn = data.get('book_isbn')

    # Retrieve user and book objects
    user = User.query.get(user_id)
    book = Book.query.get(book_isbn)

    # Check if user and book exist
    if not user:
        return jsonify({'message': 'User not found.'}), 404
    if not book:
        return jsonify({'message': 'Book not found.'}), 404

    # Create and save new rating
    rating = Rating(user=user, book=book, stars=rating_value, timestamp=datetime.utcnow())
    db.session.add(rating)
    db.session.commit()

    return '', 201