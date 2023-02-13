import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        # port="8000",
        user='postgres',
        password='212426')
#
# from config.db import conn

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS books;')

cur.execute('CREATE TABLE books (book_id serial PRIMARY KEY,'
            'title varchar (150) NOT NULL,'
            'author varchar (50) NOT NULL,'
            'description varchar NOT NULL,'
            'price float NOT NULL);')

# Insert data into the table

cur.execute('INSERT INTO books (title, author, description, price)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             'A great classic!',
             9.99)
            )


cur.execute('INSERT INTO books (title, author, description, price)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             'Another great classic!',
             12.99)
            )

cur.execute('INSERT INTO books (title, author, description, price)'
            'VALUES (%s, %s, %s, %s)',
            ('The Hobbit',
             'JK Rowling',
             'A fictitious classic!',
             12.99)
            )

conn.commit()

cur.close()

conn.close()