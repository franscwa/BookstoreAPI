from config.db import db
from config.ma import ma
from enum import Enum


class Roles(Enum):
    USER = "USER"
    ADMIN = "ADMIN"


def is_valid_role(role_name):
    return role_name is not None and role_name in get_roles()


def get_roles():
    return [role.value for role in Roles]


class Role(db.Model):
    name = db.Column(db.String, primary_key=True)
    users = db.relationship("User", back_populates="role")

    def validate(self):
        assert is_valid_role(self.name), f"role name must be one of {get_roles()}"


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True
        exclude = ("users",)
        sqla_session = db.session


role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)
