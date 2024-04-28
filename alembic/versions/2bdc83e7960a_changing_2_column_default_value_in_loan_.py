"""Changing 2 column default value in loan table

Revision ID: 2bdc83e7960a
Revises: 87edbb85fead
Create Date: 2024-04-28 12:18:17.928803

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2bdc83e7960a'
down_revision: Union[str, None] = '87edbb85fead'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('loan', 'approval_status', server_default="False")
    op.alter_column('loan', 'status', server_default="False")
    pass


def downgrade() -> None:
    pass
