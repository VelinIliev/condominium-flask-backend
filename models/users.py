from db import db
from models.enums import RoleType
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(100))
    password = db.Column(db.String(255), nullable=False)
    apartment = db.Column(db.Integer, nullable=True)
    photo = db.Column(db.String(255))

    create_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    modified_on = db.Column(db.DateTime)
    is_deleted = db.Column(db.Boolean, default=False)

    role = db.Column(
        db.Enum(RoleType),
        default=RoleType.viewer,
        nullable=False
    )
