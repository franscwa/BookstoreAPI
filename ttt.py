import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        # port="8000",
        user='postgres',
        password='212426')

# from config.db import conn

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS ratings;')

cur.execute('CREATE TABLE ratings (rating_id serial PRIMARY KEY,'
                                'rating integer NOT NULL'
                                'FORIEGN KEY (book_id) REFERENCES books(book_id);')

# Insert data into the table

cur.execute('INSERT INTO ratings (rating, book_id)'
            'VALUES (%s, %s)',
            (5, 0)
            )

cur.execute('INSERT INTO ratings (rating, book_id)'
            'VALUES (%s, %s)',
            (2, 1)
            )

conn.commit()

cur.execute('SELECT * FROM books, ratings WHERE books.book_id = ratings.book_id')

records = cur.fetchall()

for row in records:
    print("1: ", row[0])
    print("2: ", row[1])
    print("2: ", row[2])
    print("2: ", row[3])
    print("3: ", row[4], "\n")



cur.close()

conn.close()