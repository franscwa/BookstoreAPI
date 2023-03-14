from flask import Flask, request, jsonify, json, render_template
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




class Book(db.Model):
    bookid = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(50), nullable = False, unique = True)
    description = db.Column(db.Text(), nullable = False)
    price = db.Column(db.Float(), nullable = False, unique = False)
            
    
    def __init__(self, title, description, price):
        self.title = title
        self.description = description
        self.price = price
    
    def __repr__(self):
        return f"<title = {self.title} description = {self.description} price = {self.price}>" 
    
    
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



class BookSchema(Schema):
    bookid = fields.Integer()
    title = fields.String()
    description = fields.String()
    price = fields.Float()






class User(db.Model):
    userid = db.Column(Integer(), primary_key = True)
    username = db.Column(String(25), nullable = False, unique = True)
    email = db.Column(String(80), nullable = False, unique = True)
    
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def __repr__(self):
        return f"<username = {self.username} email = {self.email}>" 
    
    
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
        
    
class UserSchema(Schema):
    userid = fields.Integer()
    username = fields.String()
    email = fields.String()
    
    
    
    
    
    
    
class Wishlist(db.Model):
    wishlistid = db.Column(db.Integer(), primary_key = True)
    wishlistname = db.Column(db.String(50), nullable = False, unique = False)
    
    class WishlistSchema(Schema):
        wishlistid = fields.Integer()    
        wishlistname = fields.String()
    

    
    def __init__(self, wishlistname):
        self.wishlistname = wishlistname

    
    def __repr__(self):
        return f"<wishlistname = {self.wishlistname}>" 
    
    
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








    
@app.route('/book', methods = ['POST'])
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






@app.route('/book', methods = ['GET'])
def get_all_books():
    book = Book.get_all_books()

    serializer = BookSchema(many=True)

    data = serializer.dump(book)

    return jsonify(
        data
    )



@app.route('/book/<int:bookid>', methods = ['GET'])
def get_book(bookid):
    book = Book.get_book(bookid)

    serializer = BookSchema()

    data = serializer.dump(book)

    return jsonify(
        data
    ), 200







@app.route('/user', methods = ['POST'])
def create_user():
    data = request.get_json()

    new_user = User(
        username = data.get('username'),
        email = data.get('email'),
        
    )

    new_user.save()

    serializer = UserSchema()

    data=serializer.dump(new_user)

    return jsonify(
        data
    ), 201





@app.route('/user', methods = ['GET'])
def get_all_users():
    user = User.get_all_users()

    serializer = UserSchema(many = True)

    data = serializer.dump(user)

    return jsonify(
        data
    )





@app.route('/user/<int:userid>', methods = ['GET'])
def get_user(userid):
    user = User.get_user(userid)

    serializer = UserSchema()

    data = serializer.dump(user)

    return jsonify(
        data
    ), 200






@app.route('/user/<int:userid>', methods = ['PUT'])
def update_user(userid):
    user_to_update = User.get_user(userid)

    data = request.get_json()

    user_to_update.username = data.get('username')
    user_to_update.email = data.get('email')
    

    db.session.commit()

    serializer = UserSchema()

    user_data = serializer.dump(user_to_update)

    return jsonify(user_data), 200






@app.route('/user/<int:userid>/wishlist', methods = ['POST'])
def create_a_wishlist(userid):
    
    userid = User.get_user(userid)

    data = request.get_json()

    new_wishlist = Wishlist(
        wishlistname = data.get('wishlistname')
        
                
    )

    new_wishlist.save()

    serializer = Wishlist.WishlistSchema()

    data = serializer.dump(new_wishlist)

    return jsonify(
        data
    ), 201







@app.route('/user/<int:userid>/wishlist', methods = ['GET'])
def get_all_wishlists(userid):
    
    userid = User.get_user(userid)

    
    wishlists = Wishlist.get_all_wishlists()

    serializer = Wishlist.WishlistSchema(many = True)

    data = serializer.dump(wishlists)

    return jsonify(
        data
    )





@app.route('/user/<int:userid>/wishlist/<int:wishlistid>', methods = ['GET'])
def get_wishlist(userid, wishlistid):
    
    userid = User.get_user(userid)
    
    user = User.get_user(userid)

    wishlist = Wishlist.get_wishlist(wishlistid)
    
    serializer1 = UserSchema()

    serializer2 = Wishlist.WishlistSchema()
    
    data1 = serializer1.dump(user)

    data2 = serializer2.dump(wishlist)

    return jsonify(
        data1, data2
    ), 200






@app.route('/user/<int:userid>/wishlist/<int:wishlistid>/book/<int:bookid>', methods = ['POST'])

def add_a_wishlist_book(userid, wishlistid, bookid):
    
    userid = User.get_user(userid)
    
    wishlistid = Wishlist.get_wishlist(wishlistid)
    
    bookid = Book.get_book(bookid)
    
    bookid.save()

    serializer = BookSchema()

    data = serializer.dump(bookid)

    return jsonify(
        data
    ), 200





def init_db():
    #Initialize the database.
    with app.app_context():
        db.drop_all()
        db.create_all()
    print("database initialized")


def seed_db():
    #Seed the database.
    with app.app_context():
        book1 = Book(title = "The Hobbit", description = "A great book", price = 10.99)
        book2 = Book(title = "The Silmarillion", description = "A great book", price = 11.99)
        book3 = Book(title = "The Fellowship of the Ring", description = "A great book", price = 12.99)
        book4 = Book(title = "The Two Towers", description = "A great book", price = 13.99)
        book5 = Book(title = "The Return of the King", description = "A great book", price = 15.99)
        books = [book1, book2, book3, book4, book5]
        
        user1 = User(username = "JeremyWal", email = "jewalli@gmail.com")
        user2 = User(username = "MichaelBer", email = "mberry@gmail.com")
        users = [user1, user2]
        
        wishlist1 = Wishlist(wishlistname = "My upcoming favorites.")
        wishlists = [wishlist1]
        
        
        
        db.session.add_all(books)
        db.session.add_all(users)        
        db.session.add_all(wishlists)        
        db.session.commit()
        
    print("database seeded")
    
 
    
    
    
        
if __name__ == '__main__':
    init_db()
    seed_db()
    app.run(debug = True)