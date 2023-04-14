from config.db import db
from config.ma import ma
from models.role import is_valid_role, get_roles
from models.wishlist import Wishlist


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    role_name = db.Column(db.String, db.ForeignKey("role.name"), nullable=False)
    role = db.relationship("Role", back_populates="users")
    


    def validate(self):
        assert (
            self.first_name is not None and len(self.first_name) > 0
        ), "non-empty user first name is required"
        assert (
            self.last_name is not None and len(self.last_name) > 0
        ), "non-empty user last name is required"
        assert (
            self.email is not None and len(self.email) > 0
        ), "non-empty user email is required"
        assert (
            self.password is not None and 8 <= len(self.password) <= 32
        ), "non-empty user password of length [8-32] is required"
        assert self.role_name is not None and is_valid_role(
            self.role_name
        ), f"role_name must be one of {get_roles()}"
        
        wishlists = db.relationship('Wishlist', backref = 'user')
        
    @classmethod
    def get_user(cls, id):
        return cls.query.get_or_404(id)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        dump_only = ("user_id",)
        exclude = ("role",)
        sqla_session = db.session


user_schema = UserSchema()
users_schema = UserSchema(many=True)
