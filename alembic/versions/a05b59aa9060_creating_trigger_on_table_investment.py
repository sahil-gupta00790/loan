"""Creating trigger on table investment

Revision ID: a05b59aa9060
Revises: 031f2bfefc27
Create Date: 2024-04-28 16:59:23.375757

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a05b59aa9060'
down_revision: Union[str, None] = '031f2bfefc27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('investment','investment_date_end',type=sa.TIMESTAMP(timezone=True))
    pass


def downgrade() -> None:
    pass
