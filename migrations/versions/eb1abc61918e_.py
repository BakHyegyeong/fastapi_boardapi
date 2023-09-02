"""empty message

Revision ID: eb1abc61918e
Revises: b354461fb094
Create Date: 2023-09-02 17:24:28.155724

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'eb1abc61918e'
down_revision = 'b354461fb094'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('physicalpain', sa.Column('wrist', sa.Boolean(), nullable=False))
    op.alter_column('physicalpain', 'shoulder',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('physicalpain', 'elbow',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('physicalpain', 'finger',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('physicalpain', 'waist',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('physicalpain', 'joint',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('physicalpain', 'knee',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('physicalpain', 'ankle',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('physicalpain', 'ankle',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('physicalpain', 'knee',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('physicalpain', 'joint',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('physicalpain', 'waist',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('physicalpain', 'finger',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('physicalpain', 'elbow',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('physicalpain', 'shoulder',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.drop_column('physicalpain', 'wrist')
    # ### end Alembic commands ###
