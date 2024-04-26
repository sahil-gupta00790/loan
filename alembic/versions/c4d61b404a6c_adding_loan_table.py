"""Adding loan table

Revision ID: c4d61b404a6c
Revises: 92b251dcf7d4
Create Date: 2024-04-27 00:18:43.611680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4d61b404a6c'
down_revision: Union[str, None] = '92b251dcf7d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'loan',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('loan_amount', sa.Numeric(10,0), nullable=False),
        sa.Column('loan_type', sa.String(50), nullable=False),
        sa.Column('loan_interest', sa.Numeric(10, 2), nullable=False),
        sa.Column('loan_term', sa.Integer, nullable=False),
        sa.Column('start_date',sa.DateTime, server_default=sa.text('now()'), nullable=False),
        sa.Column('repayment_frequency',sa.Integer,nullable=False),
        sa.Column('repayment_date_next', sa.DateTime, server_default=sa.text('now()'), nullable=False),
        sa.Column('Paid_last_one?',sa.Boolean,nullable=False,default=False),                  
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
        sa.Column('approval_status',sa.Boolean,default=False),
    )
    pass


def downgrade() -> None:
    op.drop_table('loan')
    pass
