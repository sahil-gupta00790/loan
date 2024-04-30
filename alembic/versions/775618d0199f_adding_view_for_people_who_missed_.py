"""Adding view for people who missed payments

Revision ID: 775618d0199f
Revises: 7df04a78dbee
Create Date: 2024-04-28 17:32:14.475826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision: str = '775618d0199f'
down_revision: Union[str, None] = '7df04a78dbee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('loan','paid_last_one',server_default='True')
    op.execute(text('''CREATE OR REPLACE VIEW Customer_who_did_not_pay AS
                  SELECT ci.id AS customer_id,
                    ci.name ,
                    cl.email,
                    pn.phone_number,
                    co.name AS officer_name

                    FROM customer_information ci
                    JOIN phone_number pn ON ci.id = pn.customer_id
			JOIN customer_login cl ON ci.id=cl.id
                    JOIN loan_customer_officer_collateral_details lca ON ci.id = lca.customer_id
                    JOIN loan lo ON lca.loan_id = lo.id
                    JOIN employee_details co ON lca.officer_id = co.id
			WHERE lo.paid_last_one=false
                    GROUP BY ci.id, cl.email,pn.phone_number, co.name ;'''))
    pass


def downgrade() -> None:
    pass
