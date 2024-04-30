"""Adding view for non approved loans

Revision ID: 296acf0f1041
Revises: 775618d0199f
Create Date: 2024-04-28 18:02:24.584864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '296acf0f1041'
down_revision: Union[str, None] = '775618d0199f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('loan','status',type_=sa.String(15),server_default='pending')
    
    pass


def downgrade() -> None:
    pass
