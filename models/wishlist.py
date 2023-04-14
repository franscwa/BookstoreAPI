from config.db import db
from config.ma import ma
from marshmallow import Schema, fields

wishlist_books = db.Table('wishlist_books',
    db.Column('wishlistid', db.Integer, db.ForeignKey('wishlist.wishlistid'), primary_key = True) ,
    db.Column('isbn', db.String, db.ForeignKey('book.isbn'), primary_key = True)                    
)    


class Wishlist(db.Model):
    wishlistid = db.Column(db.Integer(), primary_key = True)
    wishlist_name = db.Column(db.String(50), nullable = False, unique = False)
    # Wishlist class variables
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable = False)
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
    
    