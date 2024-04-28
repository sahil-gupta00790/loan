"""Changing column approval,status , making a server_defauklt

Revision ID: fdb08f2d18d7
Revises: 1222fe2af1fd
Create Date: 2024-04-28 14:08:54.800845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdb08f2d18d7'
down_revision: Union[str, None] = '1222fe2af1fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('collateral', 'approval_status', server_default="False")
    
    pass


def downgrade() -> None:
    pass
