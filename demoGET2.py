from config.db import conn

cur = conn.cursor()

cur.execute('SELECT * FROM books, ratings WHERE books.book_id = ratings.book_id')

records = cur.fetchall()

for row in records:
    print("book_id: ", row[0])
    print("title: ", row[1])
    print("author: ", row[2])
    print("description: ", row[3])
    print("price: ", row[4])
    print("rating_id: ", row[5])
    print("rating: ", row[7], "\n")

cur.close()

conn.close()

