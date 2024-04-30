"""creating view Unapproved_Loan

Revision ID: 1905ef5c1be6
Revises: c4d800c342b3
Create Date: 2024-04-28 21:05:18.875197

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision: str = '1905ef5c1be6'
down_revision: Union[str, None] = 'c4d800c342b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(text('''CREATE OR REPLACE VIEW Non_approved_loans AS
                  SELECT ci.id AS customer_id,
                    ci.name ,
                    cl.email,
ci.income,
                    pn.phone_number,
                    lo.id as loan_id,
                    lo.loan_amount,
lo.loan_interest,
lo.loan_term,
lo.repayment_frequency

                    FROM customer_information ci
                    JOIN phone_number pn ON ci.id = pn.customer_id
			JOIN customer_login cl ON ci.id=cl.id
                    JOIN loan_customer_officer_collateral_details lca ON ci.id = lca.customer_id
                    JOIN loan lo ON lca.loan_id = lo.id
                    
			WHERE status='pending'
                    GROUP BY ci.id, cl.email,ci.income,pn.phone_number,lo.id,lo.loan_amount , lo.loan_interest, lo.loan_term , lo.repayment_frequency  ;'''))
    pass


def downgrade() -> None:
    pass
