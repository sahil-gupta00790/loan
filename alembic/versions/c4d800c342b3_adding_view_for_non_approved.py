"""Adding view for non approved 

Revision ID: c4d800c342b3
Revises: 296acf0f1041
Create Date: 2024-04-28 18:05:07.513421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision: str = 'c4d800c342b3'
down_revision: Union[str, None] = '296acf0f1041'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(text('''CREATE OR REPLACE VIEW Unapproved_loans AS
                  SELECT ci.id AS customer_id,
                    ci.name ,
                    cl.email,
ci.income,
                    pn.phone_number,
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
                    GROUP BY ci.id, cl.email,ci.income,pn.phone_number,lo.loan_amount , lo.loan_interest, lo.loan_term , lo.repayment_frequency  ;'''))
    pass


def downgrade() -> None:
    pass
