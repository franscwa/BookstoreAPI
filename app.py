from flask import Flask, jsonify
from config.config import load_config
from config.db import db
from config.ma import ma
from marshmallow.exceptions import ValidationError
from blueprints.admin import admin_bp
from blueprints.auth import auth_bp
from blueprints.authors import authors_bp
from blueprints.books import books_bp
from blueprints.ratings import ratings_bp
from blueprints.comments import comments_bp
from commands.db_cli import db_cli
from werkzeug.exceptions import HTTPException
from http import HTTPStatus


def create_app():
    app = Flask(import_name=__name__, static_folder=None)

    config = load_config()
    app.config.from_mapping(config)

    ma.init_app(app)
    db.init_app(app)

    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(authors_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(ratings_bp)
    app.register_blueprint(comments_bp)

    app.cli.add_command(db_cli)

    @app.errorhandler(Exception)
    def default_error(e):
        if isinstance(e, HTTPException):
            return jsonify(error=e.description), e.code
        elif isinstance(e, (AssertionError, ValidationError)):
            return jsonify(error=str(e)), HTTPStatus.BAD_REQUEST
        else:
            return jsonify(error=str(e)), HTTPStatus.INTERNAL_SERVER_ERROR

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=app.config["FLASK_RUN_PORT"])
