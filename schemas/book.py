from config.ma import ma
from models.book import Book


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        dump_only = ("book_id",)
        load_instance = True
