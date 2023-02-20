from flask import Flask, jsonify
from config.app_config import APP_CONFIG
from config.db import db
from config.ma import ma
from commands.db_cli import db_cli
from werkzeug.exceptions import HTTPException
from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR
from blueprints.books import books_bp
from blueprints.authors import authors_bp
from blueprints.ratings import ratings_bp
from blueprints.comments import comments_bp
from blueprints.admin import admin_bp

app = Flask(__name__)
app.config.from_mapping(APP_CONFIG)

ma.init_app(app)
db.init_app(app)

app.register_blueprint(books_bp)
app.register_blueprint(books_bp)
app.register_blueprint(authors_bp)
app.register_blueprint(ratings_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(admin_bp)


@app.errorhandler(Exception)
def default_error(e):
    if isinstance(e, HTTPException):
        return jsonify(error=e.description), e.code
    elif isinstance(e, AssertionError):
        return jsonify(error=str(e)), BAD_REQUEST
    else:
        return jsonify(error=str(e)), INTERNAL_SERVER_ERROR


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=app.config["FLASK_RUN_PORT"])
