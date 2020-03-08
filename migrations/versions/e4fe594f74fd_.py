"""empty message

Revision ID: e4fe594f74fd
Revises: 001348f4a4c5
Create Date: 2020-03-07 23:39:04.659226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4fe594f74fd'
down_revision = '001348f4a4c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('country', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'country')
    # ### end Alembic commands ###