"""account number addition for customer_details table

Revision ID: 5c8dfd81f98e
Revises: fdb08f2d18d7
Create Date: 2024-04-28 15:18:07.304495

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c8dfd81f98e'
down_revision: Union[str, None] = 'fdb08f2d18d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('customer_information', sa.Column('upi_id', sa.String(length=20), nullable=True))

    pass


def downgrade() -> None:
    pass
