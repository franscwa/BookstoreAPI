from config.db import db
from config.ma import ma


class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    biography = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String, nullable=False)

    books = db.relationship(
        "Book", back_populates="author", cascade="all, delete, delete-orphan"
    )

    def validate(self):
        assert (
            self.first_name is not None and len(self.first_name) > 0
        ), "non-empty author first name is required"
        assert (
            self.last_name is not None and len(self.last_name) > 0
        ), "non-empty author last name is required"
        assert (
            self.biography is not None and len(self.biography) > 0
        ), "non-empty author biography is required"
        assert (
            self.publisher is not None and len(self.publisher) > 0
        ), "non-empty author publisher is required"


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True
        dump_only = ("author_id",)
        exclude = ("books",)
        sqla_session = db.session


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
