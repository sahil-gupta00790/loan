"""Adding transaction  table

Revision ID: 92b251dcf7d4
Revises: 3e223c7e70da
Create Date: 2024-04-27 00:12:11.060200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92b251dcf7d4'
down_revision: Union[str, None] = '3e223c7e70da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'transaction',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('sender_id', sa.Integer, nullable=False),
        sa.Column('amount', sa.Integer, nullable=False),
        sa.Column('time', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
        sa.ForeignKeyConstraint(['sender_id'], ['customer_login.id'], ondelete='CASCADE'),
        )
    pass


def downgrade() -> None:
    op.drop_table('transaction');
    pass
