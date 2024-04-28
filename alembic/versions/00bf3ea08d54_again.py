"""Again

Revision ID: 00bf3ea08d54
Revises: fdbe1d164517
Create Date: 2024-04-28 03:11:36.572117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text

# revision identifiers, used by Alembic.
revision: str = '00bf3ea08d54'
down_revision: Union[str, None] = 'fdbe1d164517'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(text("""
       CREATE OR REPLACE FUNCTION analyzing_next_interest()
RETURNS TRIGGER AS $$
BEGIN
    -- Calculate total interest
    NEW.amount_to_be_paid_this_month := ((NEW.loan_amount * NEW.loan_interest * (NEW.loan_term*12/NEW.repayment_frequency) / 100) + NEW.loan_amount)/NEW.loan_term*12/NEW.repayment_frequency;

    -- Update the total_interest column in the newly inserted row
    UPDATE loan
    SET amount_to_be_paid_this_month = NEW.amount_to_be_paid_this_month
    WHERE id = NEW.id; -- Adjust this condition based on your table's primary key

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER analyze_next_interest_trigger
AFTER INSERT ON loan
FOR EACH ROW
EXECUTE FUNCTION analyzing_next_interest();"""))
    pass


def downgrade() -> None:
    pass
