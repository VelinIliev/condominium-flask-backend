import enum


class RoleType(enum.Enum):
    viewer = "Viewer"
    owner = "Owner"
    admin = "Admin"


class BalanceType(enum.Enum):
    income = "Income"
    expense = "Expense"
