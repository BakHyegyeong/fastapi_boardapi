"""empty message

Revision ID: 0d24b2e125af
Revises: c2b7a5f03271
Create Date: 2023-08-02 15:30:58.302312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d24b2e125af'
down_revision = 'c2b7a5f03271'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('modify_date', sa.DateTime(), nullable=True))
    op.add_column('question', sa.Column('modify_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'modify_date')
    op.drop_column('answer', 'modify_date')
    # ### end Alembic commands ###
