"""make phone nullable

Revision ID: 6aa739e0b0fd
Revises: b7c264fdfb60
Create Date: 2023-03-20 11:22:54.783788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aa739e0b0fd'
down_revision = 'b7c264fdfb60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###