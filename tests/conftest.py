import pytest
from app import create_app
from config.config import load_config


@pytest.fixture(scope="session")
def app():
    config = load_config()
    config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        }
    )
    app = create_app(config)
    app.test_cli_runner().invoke(args=["db", "migrate"])
    app.test_cli_runner().invoke(args=["db", "seed"])
    return app


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()
