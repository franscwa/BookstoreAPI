from config.db import conn

# Open a cursor to perform database operations
cur = conn.cursor()

cur.execute('SELECT * FROM books')

records = cur.fetchall()

for row in records:
    print("book_id: ", row[0])
    print("title: ", row[1])
    print("author: ", row[2])
    print("description: ", row[3])
    print("price: ", row[4], "\n")



cur.close()

conn.close()