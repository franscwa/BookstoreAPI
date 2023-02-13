from config.db import conn

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS ratings;')

cur.execute('CREATE TABLE ratings (rating_id serial,'
            'book_id integer NOT NULL,'
            'rating integer NOT NULL,'
            'PRIMARY KEY (rating_id),'
            'FOREIGN KEY (book_id) REFERENCES books(book_id));')

# Insert data into the table

cur.execute('INSERT INTO ratings (rating, book_id)'
            'VALUES (%s, %s)',
            (5, 3)
            )

cur.execute('INSERT INTO ratings (rating, book_id)'
            'VALUES (%s, %s)',
            (2, 1)
            )

cur.execute('INSERT INTO ratings (rating, book_id)'
            'VALUES (%s, %s)',
            (5, 2)
            )

cur.execute('INSERT INTO ratings (rating, book_id)'
            'VALUES (%s, %s)',
            (3, 3)
            )

cur.execute('INSERT INTO ratings (rating, book_id)'
            'VALUES (%s, %s)',
            (4, 1)
            )

conn.commit()

cur.close()

conn.close()