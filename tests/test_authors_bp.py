from http import HTTPStatus


def test_create_valid_author(client):
    author = get_dummy_author()
    response = client.post("/api/v1/authors", json=author)
    assert response.status_code == HTTPStatus.CREATED


def test_create_invalid_author_with_empty_first_name(client):
    author = get_dummy_author()
    author["first_name"] = ""
    response = client.post("/api/v1/authors", json=author)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_no_first_name(client):
    author = get_dummy_author()
    author["first_name"] = None
    response = client.post("/api/v1/authors", json=author)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_empty_last_name(client):
    author = get_dummy_author()
    author["last_name"] = ""
    response = client.post("/api/v1/authors", json=author)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_no_last_name(client):
    author = get_dummy_author()
    author["last_name"] = None
    response = client.post("/api/v1/authors", json=author)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_empty_biography(client):
    author = get_dummy_author()
    author["biography"] = ""
    response = client.post("/api/v1/authors", json=author)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_no_biography(client):
    author = get_dummy_author()
    author["biography"] = None
    response = client.post("/api/v1/authors", json=author)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_no_publisher(client):
    author = get_dummy_author()
    author["publisher"] = None
    response = client.post("/api/v1/authors", json=author)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_author_with_empty_publisher(client):
    author = get_dummy_author()
    author["publisher"] = ""
    response = client.post("/api/v1/authors", json=author)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def get_dummy_author():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "biography": "The biography for this author.",
        "publisher": "Some Publisher",
    }
