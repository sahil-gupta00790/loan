"""Creating trigger for table investment

Revision ID: 08e5576cb44a
Revises: a05b59aa9060
Create Date: 2024-04-28 17:03:41.111358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision: str = '08e5576cb44a'
down_revision: Union[str, None] = 'a05b59aa9060'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(text("""
CREATE OR REPLACE FUNCTION calculate_total_investment()
RETURNS TRIGGER AS $$
BEGIN
    -- Calculate total interest
    NEW.amount_to_be_paid := (NEW.amount * NEW.interest_rate * NEW.duration / 100) + NEW.amount;

    -- Update the total_interest column in the newly inserted row
    UPDATE investment
    SET amount_to_be_paid = NEW.amount_to_be_paid
    WHERE id = NEW.id; -- Adjust this condition based on your table's primary key

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER calculate_total_investment_trigger
AFTER INSERT ON investment
FOR EACH ROW
EXECUTE FUNCTION calculate_total_investment();"""))

    pass


def downgrade() -> None:
    pass
