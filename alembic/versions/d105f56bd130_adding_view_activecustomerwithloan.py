"""Adding view ActiveCustomerWithLoan

Revision ID: d105f56bd130
Revises: 8fe9ba757d59
Create Date: 2024-04-27 14:22:26.037219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision: str = 'd105f56bd130'
down_revision: Union[str, None] = '8fe9ba757d59'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    ql_view=text('''CREATE OR REPLACE VIEW ActiveCustomersWithLoan AS
                  SELECT ci.id AS customer_id,
                    ci.name ,
                    ci.income,
                    pn.phone_number,
                    co.name AS officer_name

                    FROM customer_information ci
                    JOIN phone_number pn ON ci.id = pn.customer_id
                    JOIN loan_customer_officer_collateral_details lca ON ci.id = lca.customer_id
                    JOIN loan lo ON lca.loan_id = lo.id
                    JOIN employee_details co ON lca.officer_id = co.id
                    GROUP BY ci.id, pn.phone_number, co.name ;''')
    
    op.execute(ql_view)

    pass


def downgrade() -> None:
    pass
