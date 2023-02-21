from config.db import db
from config.ma import ma


class Rating(db.Model):
    __tablename__ = 'ratings'
    rating_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    parent_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))

    def validate(self):
        assert self.book_id and self.book_id > 0, "non-empty book title is required"
        assert self.rating and 0 <= self.rating <= 5, "non-empty book description is required"
        assert self.price and self.price > 0, "positive book price is required"


class RatingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rating
        dump_only = ("rating_id",)
        load_instance = True
