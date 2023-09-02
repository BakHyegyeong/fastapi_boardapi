"""empty message

Revision ID: 08302c98439f
Revises: cf711e184ff9
Create Date: 2023-09-02 16:08:10.908454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08302c98439f'
down_revision = 'cf711e184ff9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('physicalpain',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('elbow', sa.Boolean(), nullable=True),
    sa.Column('finger', sa.Boolean(), nullable=True),
    sa.Column('wrist', sa.Boolean(), nullable=True),
    sa.Column('waist', sa.Boolean(), nullable=True),
    sa.Column('joint', sa.Boolean(), nullable=True),
    sa.Column('knee', sa.Boolean(), nullable=True),
    sa.Column('ankle', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('physicalpain')
    # ### end Alembic commands ###
