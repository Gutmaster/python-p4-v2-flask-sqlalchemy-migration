"""Initial migration.

Revision ID: 7607db902ab6
Revises: 
Create Date: 2024-07-27 17:26:59.071490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7607db902ab6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###
