from flask import Flask, jsonify
from config.app_config import APP_CONFIG
from config.db import db
from config.ma import ma
from blueprints.books_bp import books_bp
from blueprints.authors_bp import authors_bp
from commands.db_cli import db_cli
from werkzeug.exceptions import HTTPException
from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR

app = Flask(import_name=__name__, static_folder=None)
app.config.from_mapping(APP_CONFIG)

ma.init_app(app)
db.init_app(app)

app.register_blueprint(books_bp)
app.register_blueprint(authors_bp)

app.cli.add_command(db_cli)


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
