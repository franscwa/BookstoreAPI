from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, String, Integer, Float
from flask_marshmallow import Marshmallow
from marshmallow import Schema,fields


#run in Python interpretor
#from app import db
#db.create_all()

app = Flask(__name__)

app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@localhost/bookstore'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)






class User(db.Model):
    userid = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(25), nullable = False, unique = True)
    email = db.Column(db.String(80), nullable = False, unique = True)
    # User class variables
    
    wishlists = db.relationship('Wishlist', backref = 'user')
    # Establishes relationship from user to wishlist
    

    @classmethod
    def get_all_users(cls):
        return cls.query.all()
    
    @classmethod
    def get_user(cls, id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        # Class methods
       
    
class UserSchema(Schema):
    userid = fields.Integer()
    username = fields.String()
    email = fields.String()
    # User Scehma

    
    
    
    
    
    
wishlist_books = db.Table('wishlist_books',
    db.Column('wishlistid', db.Integer, db.ForeignKey('wishlist.wishlistid'), primary_key = True) ,
    db.Column('bookid', db.Integer, db.ForeignKey('book.bookid'), primary_key = True)                    
)    
# Links wishlist and book tables using a foreign key
    
    
    
    
    
class Wishlist(db.Model):
    wishlistid = db.Column(db.Integer(), primary_key = True)
    wishlist_name = db.Column(db.String(50), nullable = False, unique = False)
    # Wishlist class variables
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.userid'), nullable = False)
    # Creates foreign key for user
        
    wishlistbooks = db.relationship('Book', secondary = wishlist_books, backref = 'wishlist') 
    # Establishes the relationship between wishlist and book to create wishlistbooks


    @classmethod
    def get_all_wishlists(cls):
        return cls.query.all()
    
    @classmethod
    def get_wishlist(cls, id):
        return cls.query.get_or_404(id)
       
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        # Class methods



class WishlistSchema(Schema):
    wishlistid = fields.Integer()    
    wishlist_name = fields.String()
    # Wishlist Schema
    
    
    
    
    

class Book(db.Model):
    bookid = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(50), nullable = False, unique = True)
    description = db.Column(db.Text(), nullable = False)
    price = db.Column(db.Float(), nullable = False, unique = False)
    # Class variables
    
    wishlistid = db.Column(db.Integer, db.ForeignKey('wishlist.wishlistid'))
    # Creates foreign key for wishlist     
       
  
    
    @classmethod
    def get_all_books(cls):
        return cls.query.all()
    
    @classmethod
    def get_book(cls, id):
        return cls.query.get_or_404(id)
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        # Class methods
        



class BookSchema(Schema):
    bookid = fields.Integer()
    title = fields.String()
    description = fields.String()
    price = fields.Float()
    # Book Schema



    


    
@app.route('/api/v1/book', methods = ['POST'])
def create_a_book():
    
    data = request.get_json()

    new_book = Book(
        name = data.get('title'),
        description = data.get('description'),
        price = data.get('price'),
        
    )

    new_book.save()

    serializer = BookSchema()

    data = serializer.dump(new_book)
    

    return jsonify(
        data
    ), 201
# Route and simple instructions for creating a book    






@app.route('/api/v1/book', methods = ['GET'])
def get_all_books():
    
    book = Book.get_all_books()

    serializer = BookSchema(many = True)

    data = serializer.dump(book)

    return jsonify(
        data
    )
# Route and simple instructions for obtaining all book    s





@app.route('/api/v1/book/<int:bookid>', methods = ['GET'])
def get_book(bookid):
    
    book = Book.get_book(bookid)

    serializer = BookSchema()

    data = serializer.dump(book)

    return jsonify(
        data
    ), 200
# Route and simple instructions for obtaining a book    






@app.route('/api/v1/user', methods = ['POST'])
def create_user():
    
    data = request.get_json()

    new_user = User(
        username = data.get('username'),
        email = data.get('email'),
        
    )

    new_user.save()

    serializer = UserSchema()

    data = serializer.dump(new_user)

    return jsonify(
        data
    ), 201
# Route and simple instructions for creating a user    





@app.route('/api/v1/user', methods = ['GET'])
def get_all_users():
    
    user = User.get_all_users()

    serializer = UserSchema(many = True)

    data = serializer.dump(user)

    return jsonify(
        data
    )
# Route and simple instructions for obtaining all users    





@app.route('/api/v1/user/<int:userid>', methods = ['GET'])
def get_user(userid):
    
    user = User.get_user(userid)

    serializer = UserSchema()

    data = serializer.dump(user)

    return jsonify(
        data
    ), 200
# Route and simple instructions for obtaining a user





@app.route('/api/v1/user/<int:userid>/wishlist', methods = ['POST'])
def create_a_wishlist(userid):
    
    data = request.get_json()
    
    user_data = request.get_json()
    
    get_userid = user_data.get('userid')


    new_wishlist = Wishlist(wishlist_name = data.get('wishlist_name'),
                       user_id = data.get('userid') 
    )
        
    new_wishlist.save()
    
    db.session.commit()

    serializer = WishlistSchema()

    data = serializer.dump(new_wishlist)

    return jsonify(
    ), 201
# Route and code for creating a wishlist    
    





@app.route('/api/v1/user/<int:userid>/wishlist/<int:wishlistid>/book', methods = ['POST'])

def add_a_wishlist_book(userid, wishlistid):
    
    user = User.get_user(userid)
    
    wishlist_data = request.get_json()
    
    get_the_wishlistid = wishlist_data.get('wishlistid')
    
    book_data = request.get_json()
    
    get_bookid = book_data.get('bookid')
        
    get_wishlistid = Wishlist.query.filter_by(wishlistid = wishlistid).first()
    get_book_to_add = Book.query.filter_by(bookid = get_bookid).first()
    
    get_wishlistid.wishlistbooks.append(get_book_to_add)
    
    db.session.commit()      
    
    return jsonify(
    ), 200
# Route and code for adding a book to the wishlist    
    
    
    
    
@app.route('/api/v1/user/<int:userid>/wishlist/<int:wishlistid>/book/<int:bookid>', methods = ['DELETE'])

def delete_wishlist_book(userid, wishlistid, bookid):
    
    user = User.get_user(userid)
        
    wishlist_data = request.get_json()
    
    book_data = request.get_json()
    
    get_wishlist_data = wishlist_data.get('wishlistid')
    
    get_book_data = book_data.get('bookid')
        
    get_wishlistid = Wishlist.query.filter_by(wishlistid = wishlistid).first()
    get_book_to_delete = Book.query.filter_by(bookid = bookid).first()
             
    get_wishlistid.wishlistbooks.remove(get_book_to_delete)
    
    db.session.commit()    
    
    return jsonify(
    ), 200    
# Route and code for deleteing a book from the wishlist    
   
    
    
    
@app.route('/api/v1/user/<int:userid>/wishlist/<int:wishlistid>/book', methods = ['GET'])

def get_all_wishlist_books(userid, wishlistid):
    
    userid = User.get_user(userid)
    
    wishlist_data = request.get_json()

    get_wishlist_data = wishlist_data.get('wishlistid')
    
    wishlistid = Wishlist.get_wishlist(wishlistid)        

    wishlistbooks = wishlistid.wishlistbooks   
        
    serializer = BookSchema(many = True)
    
    data = serializer.dump(wishlistbooks)
    
    return jsonify(
        data
    ), 200
# Route and code for obtaining all books in a wishlist    
    
    
    





def init_db():
    #Initialize the database.
    with app.app_context():
        db.drop_all() # ?
        db.create_all()
    print("database initialized")


def seed_db():
    #Seed the database.
    with app.app_context():
        
        user1 = User(username = "JeremyWal", email = "jerwalli@gmail.com")
        user2 = User(username = "MichaelBer", email = "mberry@gmail.com")
        users = [user1, user2]
        
        book1 = Book(title = "The Hobbit", description = "A great book", price = 10.99)
        book2 = Book(title = "The Silmarillion", description = "A great book", price = 11.99)
        book3 = Book(title = "The Fellowship of the Ring", description = "A great book", price = 12.99)
        book4 = Book(title = "The Two Towers", description = "A great book", price = 13.99)
        book5 = Book(title = "The Return of the King", description = "A great book", price = 15.99)
        books = [book1, book2, book3, book4, book5]
        
        wishlist1 = Wishlist(wishlist_name = "My upcoming favorites.", 
                             user_id = 1, wishlistbooks = [book1, book2])
        
        wishlist2 = Wishlist(wishlist_name = "My List", 
                             user_id = 2, wishlistbooks = [book3, book5])        
        
        wishlists = [wishlist1, wishlist2]
        
        
        db.session.add_all(users)        
        db.session.add_all(books)
        db.session.add_all(wishlists)
        db.session.commit()
        
    print("database seeded")
    
# Code to seed the database 
    
    
    
        
if __name__ == '__main__':
    init_db()
    seed_db()
    #db.session.commit() ?
    app.run(debug = True)
    
# NOTE: For some reason my computer has port 8080 turned off, so the 
# server will have to run on the default port (5000)    