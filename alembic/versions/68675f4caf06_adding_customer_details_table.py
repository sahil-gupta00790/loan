"""Adding customer_details table

Revision ID: 68675f4caf06
Revises: 84f9e8f72fde
Create Date: 2024-04-27 00:01:55.261194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68675f4caf06'
down_revision: Union[str, None] = '84f9e8f72fde'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'customer_information',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('Name', sa.String(50), nullable=False),
        sa.Column('pan card', sa.String(12), nullable=False,unique=True),
        sa.Column('aadhar card', sa.NUMERIC(12,0), nullable=False,unique=True),
        sa.Column('address', sa.String(1000), nullable=False),
        sa.Column('employment_type',sa.String(50),nullable=False),
        sa.Column('income',sa.Numeric(10,0),nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
        sa.ForeignKeyConstraint(['id'], ['customer_login.id'], ondelete='CASCADE'),
        )
    


def downgrade() -> None:
    op.drop_table('customer_information')
    pass
