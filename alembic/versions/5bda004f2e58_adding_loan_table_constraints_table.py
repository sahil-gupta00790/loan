"""Adding loan table constraints  table

Revision ID: 5bda004f2e58
Revises: c4d61b404a6c
Create Date: 2024-04-27 00:19:41.049615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bda004f2e58'
down_revision: Union[str, None] = 'c4d61b404a6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'loan_customer_officer_collateral_details',
        sa.Column('loan_id',sa.Integer,nullable=False),
        sa.Column('customer_id',sa.Integer,nullable=False),
        sa.Column('officer_id',sa.Integer,nullable=False),
        sa.Column('collateral_id',sa.Integer,nullable=False),
        sa.ForeignKeyConstraint(['collateral_id'], ['collateral.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['customer_id'], ['customer_login.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['loan_id'], ['loan.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['officer_id'], ['employee_login.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('loan_id')

    )
    pass


def downgrade() -> None:
    op.drop_table('loan_customer_officer_collateral_details')
    pass
