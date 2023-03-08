from config.db import db
from config.ma import ma
from datetime import datetime


class Rating(db.Model):
    rating_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    books_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    timestamp = db.Column(db.DateTime, nullable=False)

    def validate(self):
        assert int(self.books_id) and int(self.books_id) > 0, "non-empty book title is required"
        assert int(self.rating) and 0 <= int(self.rating) <= 5, "non-empty book description is required"


class RatingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rating
        dump_only = ("rating_id",)
        load_instance = True
