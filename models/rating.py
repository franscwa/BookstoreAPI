from config.db import db
from config.ma import ma
from datetime import datetime


class Rating(db.Model):
    rating_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    isbn = db.Column(db.String, db.ForeignKey("book.isbn"), nullable=False)
    book = db.relationship("Book", back_populates="ratings")

    def validate(self):
        assert 0 < int(self.isbn) < 9999999999, "non-empty book title is required"
        assert (
            int(self.rating) and 0 <= int(self.rating) <= 5
        ), "non-empty book description is required"


class RatingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rating
        dump_only = ("rating_id",)
        exclude = ("book",)
        load_instance = True


rating_schema = RatingSchema()
ratings_schema = RatingSchema(many=True)
