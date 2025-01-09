"""empty message

Revision ID: 9fa41b7bbb72
Revises: 6ebb523edd4c
Create Date: 2024-06-15 19:51:03.202615

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9fa41b7bbb72'
down_revision = '6ebb523edd4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_column('full_desc')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('full_desc', mysql.TEXT(), nullable=False))

    # ### end Alembic commands ###
