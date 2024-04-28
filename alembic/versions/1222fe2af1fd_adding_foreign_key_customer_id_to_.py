"""adding foreign key customer_id to collateral

Revision ID: 1222fe2af1fd
Revises: d560f80f4d34
Create Date: 2024-04-28 13:59:38.645700

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1222fe2af1fd'
down_revision: Union[str, None] = 'd560f80f4d34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Step 1: Add the 'customer_id' column to 'collateral' table
    op.add_column('collateral', sa.Column('customer_id', sa.Integer(), nullable=True))# Step 2: Add the foreign key constraint referencing 'customer_login' table
    op.create_foreign_key('fk_customer_id', 'collateral', 'customer_login', ['customer_id'], ['id'], ondelete='CASCADE')



pass



def downgrade() -> None:
    pass
