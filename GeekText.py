from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route("/books/genre", methods=["GET"])
def books_by_genre():
    genre = request.args.get("genre")
    # Connect to the database and retrieve a list of books for the given genre
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="bookstore"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE genre = %s", (genre,))
    books = cursor.fetchall()
    conn.close()
    # Return the list of books in JSON format
    return {"books": books}

@app.route("/books/topsellers", methods=["GET"])
def top_sellers():
    # Connect to the database and retrieve the top 10 selling books
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="bookstore"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book ORDER BY copies_sold DESC LIMIT 10")
    books = cursor.fetchall()
    conn.close()
    # Return the list of books in JSON format
    return {"books": books}

@app.route("/books/rating", methods=["GET"])
def books_by_rating():
    rating = request.args.get("rating")
    # Connect to the database and retrieve a list of books with a rating higher or equal to the passed value
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="bookstore"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE rating >= %s", (rating,))
    books = cursor.fetchall()
    conn.close()
    # Return the list of books in JSON format
    return {"books": books}

@app.route("/books/discount", methods=["PUT"])
def discount_books():
    publisher = request.args.get("publisher")
    discount = request.args.get("discount")
    # Connect to the database and update the price of all books under a publisher by the discount percent
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="bookstore"
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE book SET price =  price - (price * %s) / 100  WHERE publisher = %s", (discount, publisher))
    conn.commit()
    conn.close()
    # Return a success message
    return {"message": "Books under the publisher have been updated"}

if __name__ == "__main__":
    app.run(debug=True)

