"""merge heads

Revision ID: 35b8aa90e698
Revises: 99933ba0a787, eb1abc61918e
Create Date: 2023-10-11 15:08:27.993162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35b8aa90e698'
down_revision = ('99933ba0a787', 'eb1abc61918e')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
