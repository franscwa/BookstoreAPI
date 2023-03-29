import random
from http import HTTPStatus


def test_create_valid_book(client):
    book = get_dummy_book()
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.CREATED


def test_create_invalid_book_with_empty_isbn(client):
    book = get_dummy_book()
    book["isbn"] = ""
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_no_isbn(client):
    book = get_dummy_book()
    book["isbn"] = None
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_invalid_isbn(client):
    book = get_dummy_book()
    book["isbn"] = "123"
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_duplicate_isbn(client):
    book1 = get_dummy_book()
    response = client.post("/api/v1/books", json=book1)
    assert response.status_code == HTTPStatus.CREATED
    book2 = get_dummy_book()
    book2["isbn"] = book1["isbn"]
    response = client.post("/api/v1/books", json=book1)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_empty_title(client):
    book = get_dummy_book()
    book["title"] = ""
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_no_title(client):
    book = get_dummy_book()
    book["title"] = None
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_duplicate_title(client):
    book1 = get_dummy_book()
    response = client.post("/api/v1/books", json=book1)
    assert response.status_code == HTTPStatus.CREATED
    book2 = get_dummy_book()
    book2["title"] = book2["title"]
    response = client.post("/api/v1/books", json=book1)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_empty_description(client):
    book = get_dummy_book()
    book["description"] = ""
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_no_description(client):
    book = get_dummy_book()
    book["description"] = None
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_empty_price(client):
    book = get_dummy_book()
    book["price"] = ""
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_no_price(client):
    book = get_dummy_book()
    book["price"] = None
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_invalid_price(client):
    book = get_dummy_book()
    book["price"] = "abc"
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_zero_price(client):
    book = get_dummy_book()
    book["price"] = 0
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_negative_price(client):
    book = get_dummy_book()
    book["price"] = -1
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_empty_publisher(client):
    book = get_dummy_book()
    book["publisher"] = ""
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_no_publisher(client):
    book = get_dummy_book()
    book["publisher"] = None
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_empty_year(client):
    book = get_dummy_book()
    book["year"] = ""
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_no_year(client):
    book = get_dummy_book()
    book["year"] = None
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_invalid_year(client):
    book = get_dummy_book()
    book["year"] = "abc"
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_zero_year(client):
    book = get_dummy_book()
    book["year"] = 0
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_negative_year(client):
    book = get_dummy_book()
    book["year"] = -1
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_empty_copies_sold(client):
    book = get_dummy_book()
    book["copies_sold"] = ""
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_no_copies_sold(client):
    book = get_dummy_book()
    book["copies_sold"] = None
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_invalid_copies_sold(client):
    book = get_dummy_book()
    book["copies_sold"] = "abc"
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_zero_copies_sold(client):
    book = get_dummy_book()
    book["copies_sold"] = 0
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.CREATED


def test_create_invalid_book_with_negative_copies_sold(client):
    book = get_dummy_book()
    book["copies_sold"] = -1
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_empty_author_id(client):
    book = get_dummy_book()
    book["author_id"] = ""
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_no_author_id(client):
    book = get_dummy_book()
    book["author_id"] = None
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_invalid_author_id(client):
    book = get_dummy_book()
    book["author_id"] = "abc"
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_zero_author_id(client):
    book = get_dummy_book()
    book["author_id"] = 0
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_negative_author_id(client):
    book = get_dummy_book()
    book["author_id"] = -1
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_invalid_number_author_id(client):
    book = get_dummy_book()
    book["author_id"] = 999999
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_create_invalid_book_with_empty_genre_name(client):
    book = get_dummy_book()
    book["genre_name"] = ""
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_no_genre_name(client):
    book = get_dummy_book()
    book["genre_name"] = None
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_create_invalid_book_with_invalid_genre_name(client):
    book = get_dummy_book()
    book["genre_name"] = "non-existing-genre"
    response = client.post("/api/v1/books", json=book)
    assert response.status_code == HTTPStatus.NOT_FOUND


def get_dummy_book():
    return {
        "isbn": str(random.randint(1000000000000, 9999999999999)),
        "title": "Some Book" + str(random.randint(1000000000000, 9999999999999)),
        "description": "Some description.",
        "price": random.randint(1, 100),
        "publisher": "Some Publisher",
        "year": random.randint(1900, 2020),
        "copies_sold": random.randint(0, 100),
        "genre_name": "Fantasy",
        "author_id": 1,
    }
