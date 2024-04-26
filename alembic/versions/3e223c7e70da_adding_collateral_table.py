"""Adding collateral table

Revision ID: 3e223c7e70da
Revises: 716d4325cffe
Create Date: 2024-04-27 00:11:30.932218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e223c7e70da'
down_revision: Union[str, None] = '716d4325cffe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'collateral',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String(500), nullable=False),
        sa.Column('value', sa.Numeric(10,0), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
        sa.Column('approval_status',sa.Boolean,default=False),
    )

    pass


def downgrade() -> None:
    op.drop_table('collateral')
    pass
