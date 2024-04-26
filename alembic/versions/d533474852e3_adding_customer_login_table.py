"""Adding customer_login table

Revision ID: d533474852e3
Revises: 
Create Date: 2024-04-26 23:59:30.897787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd533474852e3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'customer_login',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), nullable=False,unique=True),
        sa.Column('password', sa.String(250), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
        
        
        )
    
    pass


def downgrade() -> None:
    op.drop_table('customer_login')
    pass
