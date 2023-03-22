from db import db
from models.enums import BalanceType
from datetime import datetime


class Income(db.Model):
    __tablename__ = 'incomes'

    id = db.Column(db.Integer, primary_key=True)
    type_of_balance = db.Column(
        db.Enum(BalanceType),
        nullable=False
    )
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    date_of_event = db.Column(db.DateTime, nullable=False)
    date_of_entry = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    document = db.Column(db.String(255), nullable=False)


# qry = db.query(Income).filter(Income.birthday.between('1985-01-17', '1988-01-17'))
