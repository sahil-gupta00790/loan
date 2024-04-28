"""Adding status to loan table

Revision ID: e4226c3f4579
Revises: d105f56bd130
Create Date: 2024-04-27 21:53:16.768830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4226c3f4579'
down_revision: Union[str, None] = 'd105f56bd130'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('loan',sa.Column('status', sa.Boolean(), server_default='false'))
    pass


def downgrade() -> None:
    pass
