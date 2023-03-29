from flask import Flask, jsonify
from config.config import load_config
from config.db import db
from config.ma import ma
from marshmallow.exceptions import ValidationError
from blueprints.books_bp import books_bp
from blueprints.authors_bp import authors_bp
from commands.db_cli import db_cli
from werkzeug.exceptions import HTTPException
from http import HTTPStatus


def create_app(cfg):
    a = Flask(import_name=__name__, static_folder=None)
    a.config.from_mapping(cfg)

    ma.init_app(a)
    db.init_app(a)

    a.register_blueprint(books_bp)
    a.register_blueprint(authors_bp)

    a.cli.add_command(db_cli)

    @a.errorhandler(Exception)
    def default_error(e):
        if isinstance(e, HTTPException):
            return jsonify(error=e.description), e.code
        elif isinstance(e, (AssertionError, ValidationError)):
            return jsonify(error=str(e)), HTTPStatus.BAD_REQUEST
        else:
            return jsonify(error=str(e)), HTTPStatus.INTERNAL_SERVER_ERROR

    return a


if __name__ == "__main__":
    config = load_config()
    app = create_app(config)
    app.run(host="0.0.0.0", port=app.config["FLASK_RUN_PORT"])
