from datetime import datetime
from config.db import db
from config.ma import ma

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('ratings', lazy=True))
    book_isbn = db.Column(db.String(13), db.ForeignKey('book.isbn'), nullable=False)
    book = db.relationship('Book', backref=db.backref('ratings', lazy=True))
    stars = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, user, book, stars):
        self.user = user
        self.book = book
        self.stars = stars

    def validate(self):
        assert self.rating is not None and self.rating >= 1 and self.rating <= 5, "rating must be between 1 and 5"

class RatingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rating
        load_instance = True
        sqla_session = db.session
