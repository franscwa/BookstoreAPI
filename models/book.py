from config.db import db
from config.ma import ma
from models.wishlist import Wishlist

class Book(db.Model):
    isbn = db.Column(db.String(13), primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    copies_sold = db.Column(db.Integer, nullable=False, default=0)

    genre_name = db.Column(db.String, db.ForeignKey("genre.name"))
    genre = db.relationship("Genre", back_populates="books")

    author_id = db.Column(db.Integer, db.ForeignKey("author.author_id"), nullable=False)
    author = db.relationship("Author", back_populates="books")

    ratings = db.relationship("Rating", back_populates="book")

    comments = db.relationship("Comment", back_populates="book")
    
    wishlistid = db.Column(db.Integer, db.ForeignKey('wishlist.wishlistid'))

    def validate(self):
        assert self.isbn is not None and len(self.isbn) == 13, "isbn must be 13 digits"
        assert (
            self.title is not None and len(self.title) > 0
        ), "non-empty book title is required"
        assert (
            self.description is not None and len(self.description) > 0
        ), "non-empty book description is required"
        assert (
            self.price is not None and self.price > 0
        ), "book price must be greater than zero"
        assert (
            self.publisher is not None and len(self.publisher) > 0
        ), "non-empty book publisher is required"
        assert (
            self.year is not None and self.year > 0
        ), "book year must be greater than zero"
        assert self.copies_sold is None or (
            self.copies_sold is not None and self.copies_sold >= 0
        ), "book copies sold must be greater than or equal to zero"
        assert (
            self.author_id is not None and self.author_id > 0
        ), "book author id must be greater than zero"
        assert (
            self.genre_name is not None and len(self.genre_name) > 0
        ), "non-empty book genre name is required"


    @classmethod
    def get_all_books(cls):
        return cls.query.all()
    
    @classmethod
    def get_book(cls, id):
        return cls.query.get_or_404(id)
    
class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        include_fk = True
        dump_only = ("book_id",)
        exclude = ("genre", "author", "ratings", "comments")
        sqla_session = db.session


book_schema = BookSchema()
books_schema = BookSchema(many=True)
