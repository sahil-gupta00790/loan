"""finally creating my first stored procedure

Revision ID: 87edbb85fead
Revises: 00bf3ea08d54
Create Date: 2024-04-28 03:17:24.028843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text

# revision identifiers, used by Alembic.
revision: str = '87edbb85fead'
down_revision: Union[str, None] = '00bf3ea08d54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(text("""
                   
        CREATE OR REPLACE FUNCTION update_loan_repayment_date()
RETURNS void AS $$
DECLARE
    loan_record RECORD;
BEGIN
    FOR loan_record IN SELECT * FROM loan WHERE repayment_date_next = CURRENT_DATE - INTERVAL '1 month' AND amount > 0 LOOP
        IF loan_record.frequency = 1 THEN
            loan_record.repayment_date_next := loan_record.repayment_date_next + 1; -- Assuming monthly means 1 month
        ELSIF loan_record.frequency = 3 THEN
            loan_record.repayment_date_next := loan_record.repayment_date_next + 3; -- Assuming quarterly means 3 months
        ELSIF loan_record.frequency = 6 THEN
            loan_record.repayment_date_next := loan_record.repayment_date_next + 6; -- Assuming annually means 12 months
        END IF;
        
        IF loan_record.amount = 0 THEN
            loan_record.paid_last_one := true;
        ELSE
            loan_record.paid_last_one := false;
        END IF;
        
        -- Check if the repayment_date_next matches the current date before updating it
        IF loan_record.repayment_date_next = CURRENT_DATE THEN
            UPDATE loan SET repayment_date_next = loan_record.repayment_date_next, paid_last_time = loan_record.paid_last_time WHERE id = loan_record.id;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;"""));




def downgrade() -> None:
    pass
