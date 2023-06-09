"""add username field

Revision ID: 9ccb664784a3
Revises: e341c901745b
Create Date: 2023-04-18 20:30:53.909526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ccb664784a3'
down_revision = 'e341c901745b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
