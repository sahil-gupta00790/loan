"""Changing 1 column default value in loan table

Revision ID: d5ba04ebc15e
Revises: 2bdc83e7960a
Create Date: 2024-04-28 12:19:53.853660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5ba04ebc15e'
down_revision: Union[str, None] = '2bdc83e7960a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('loan', 'paid_last_one', server_default="False")
    pass


def downgrade() -> None:
    pass
