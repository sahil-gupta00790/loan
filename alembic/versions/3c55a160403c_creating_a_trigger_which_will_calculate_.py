"""Creating a trigger which will calculate the total amount to be payed

Revision ID: 3c55a160403c
Revises: 77afaf2ba176
Create Date: 2024-04-28 01:15:43.498253

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text

# revision identifiers, used by Alembic.
revision: str = '3c55a160403c'
down_revision: Union[str, None] = '77afaf2ba176'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(text("""
       CREATE OR REPLACE FUNCTION calculate_total_interest()
RETURNS TRIGGER AS $$
BEGIN
    -- Calculate total interest
    NEW.amount_to_be_paid := (NEW.loan_amount * NEW.loan_interest * NEW.loan_term / 100) + NEW.loan_amount;

    -- Update the total_interest column in the newly inserted row
    UPDATE loan
    SET amount_to_be_paid = NEW.amount_to_be_paid
    WHERE id = NEW.id; -- Adjust this condition based on your table's primary key

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER calculate_total_interest_trigger
AFTER INSERT ON loan
FOR EACH ROW
EXECUTE FUNCTION calculate_total_interest();




    """))
    pass


def downgrade() -> None:
    op.execute(text("""
        DROP TRIGGER calculate_total_interest
        """))
    pass
