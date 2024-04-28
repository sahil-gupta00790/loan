"""Changing column officer , officer_id can be null

Revision ID: d560f80f4d34
Revises: d5ba04ebc15e
Create Date: 2024-04-28 13:49:27.631332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd560f80f4d34'
down_revision: Union[str, None] = 'd5ba04ebc15e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('loan_customer_officer_collateral_details','officer_id',nullable=True)
    pass


def downgrade() -> None:
    pass
