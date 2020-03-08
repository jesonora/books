"""empty message

Revision ID: 001348f4a4c5
Revises: 
Create Date: 2020-03-07 22:31:07.929233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001348f4a4c5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('published', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
