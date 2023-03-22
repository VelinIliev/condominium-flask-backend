from datetime import datetime, timedelta

import jwt
from decouple import config
from jwt import DecodeError
from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from models import User
from db import db


class AuthManager:
    @staticmethod
    def create_user(user_data):
        user_data['password'] = generate_password_hash(user_data['password'])
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def login_user(user_data):
        user = User.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Invalid email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest(f"Invalid email or password")

        return user

    @staticmethod
    def encode_token(user):
        payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(days=2)
        }

        return jwt.encode(payload, config('JWT_KEY'))

    @staticmethod
    def decode_token(token):
        try:
            return jwt.decode(token, key=config('JWT_KEY'), algorithms=['HS256'])
        except DecodeError as ex:
            raise BadRequest('Invalid or missing token')
