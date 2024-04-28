"""Adding views

Revision ID: 4d7c6245147d
Revises: eb5848122b06
Create Date: 2024-04-27 13:44:03.130475

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision: str = '4d7c6245147d'
down_revision: Union[str, None] = 'eb5848122b06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('customer_information','Name',new_column_name='name')
    pass


def downgrade() -> None:
    
    pass
