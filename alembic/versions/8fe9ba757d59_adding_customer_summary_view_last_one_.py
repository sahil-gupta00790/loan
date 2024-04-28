"""Adding customer_summary view , last one was again used for another purpose

Revision ID: 8fe9ba757d59
Revises: 2cb1d13d632b
Create Date: 2024-04-27 14:20:13.765414

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision: str = '8fe9ba757d59'
down_revision: Union[str, None] = '2cb1d13d632b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sql_view=text('''CREATE OR REPLACE VIEW Customer_summary AS
                  SELECT ci.id AS customer_id,
                    ci.name ,
                    ci.aadhaar_number, 
                    ci.income,
                    pn.phone_number,
                    co.name AS officer_name,
                
                    SUM(lo.loan_amount) AS total_loan_amount
                    FROM customer_information ci
                    JOIN phone_number pn ON ci.id = pn.customer_id
                    JOIN loan_customer_officer_collateral_details lca ON ci.id = lca.customer_id
                    JOIN loan lo ON lca.loan_id = lo.id
                    JOIN employee_details co ON lca.officer_id = co.id
                    GROUP BY ci.id, ci.name, ci.aadhaar_number, ci.income, pn.phone_number,co.name;''')
    
    op.execute(sql_view)

def downgrade() -> None:

    op.execute("DROP VIEW Customer_summary")
    pass