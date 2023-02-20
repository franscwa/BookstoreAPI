from config.db import db
from config.ma import ma


class Genre(db.Model):
    name = db.Column(db.String, primary_key=True)
    books = db.relationship("Book", back_populates="genre")


class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
        load_instance = True
        exclude = ("books",)
        sqla_session = db.session


genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
