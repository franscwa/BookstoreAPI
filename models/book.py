from config.db import db
from config.ma import ma


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    # ratings = db.relationship('rating', backref='book', lazy=True)

    def validate(self):
        assert self.title and len(self.title) > 0, "non-empty book title is required"
        assert (
            self.description and len(self.description) > 0
        ), "non-empty book description is required"
        assert self.price and self.price > 0, "positive book price is required"


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        dump_only = ("book_id",)
        load_instance = True
