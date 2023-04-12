import os
import pytest
from app import create_app


@pytest.fixture(scope="session")
def app():
    os.environ.update(
        {
            "TESTING": "True",
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        }
    )
    app = create_app()
    app.test_cli_runner().invoke(args=["db", "migrate"])
    app.test_cli_runner().invoke(args=["db", "seed"])
    return app


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()
