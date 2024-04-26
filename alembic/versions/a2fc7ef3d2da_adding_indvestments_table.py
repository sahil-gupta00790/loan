"""Adding indvestments table

Revision ID: a2fc7ef3d2da
Revises: 5bda004f2e58
Create Date: 2024-04-27 00:20:22.063655

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2fc7ef3d2da'
down_revision: Union[str, None] = '5bda004f2e58'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'investment',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('customer_id', sa.Integer, nullable=False),
        sa.Column('amount', sa.Integer, nullable=False),
        sa.Column('time', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
        sa.Column('interest_rate', sa.NUMERIC(2,2), nullable=False),
        sa.ForeignKeyConstraint(['customer_id'], ['customer_login.id'], ondelete='CASCADE'),
        )
    pass


def downgrade() -> None:
    op.drop_table('investment')
    pass
