import re

from marshmallow import Schema, fields, ValidationError, validates

from models import User


class UserRegisterRequestSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    apartment = fields.Integer(required=True)
    phone = fields.String()
    photo = fields.String()

    @validates('apartment')
    def validate_apartment(self, value):
        if value < 1 or value > 8:
            raise ValidationError('Not a valid apartment')

    @validates('email')
    def validate_unique_email(self, value):
        user = User.query.filter(User.email == value).first()
        if user:
            raise ValidationError('User with this email already exist')

    @validates('first_name')
    def validate_first_name(self, value):
        if not value:
            raise ValidationError('First name can not be empty string')

    @validates('last_name')
    def validate_last_name(self, value):
        if not value:
            raise ValidationError('Last name can not be empty string')

    @validates('password')
    def validate_password(self, value):
        length_error = len(value) < 8
        digit_error = re.search(r"\d", value) is None
        uppercase_error = re.search(r"[A-Z]", value) is None
        lowercase_error = re.search(r"[a-z]", value) is None
        symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', value) is None

        if any([length_error, digit_error, uppercase_error, lowercase_error, symbol_error]):
            raise ValidationError({
                'length_error': 'password must be at least 8 symbols' if length_error else None,
                'digit_error': 'password must include at least one number' if digit_error else None,
                'uppercase_error': 'password must include at least one upper case letter' if uppercase_error else None,
                'lowercase_error': 'password must include at least one lower case letter' if lowercase_error else None,
                'symbol_error': 'password must include at least one special character' if symbol_error else None,
            })


class UserLoginRequestSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
