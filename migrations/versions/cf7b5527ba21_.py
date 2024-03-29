"""empty message

Revision ID: cf7b5527ba21
Revises: 5f9d10e285a9
Create Date: 2023-08-10 16:01:20.010864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf7b5527ba21'
down_revision = '5f9d10e285a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('tag', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'tag')
    # ### end Alembic commands ###
