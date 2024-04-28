"""Creating a trigger for updating total_amount_paid and next month's amount to be paid , as well as updating paid_last_one?

Revision ID: 77afaf2ba176
Revises: 80c1fbcc8770
Create Date: 2024-04-27 22:14:36.784181

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision: str = '77afaf2ba176'
down_revision: Union[str, None] = '80c1fbcc8770'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(text("""
        CREATE OR REPLACE FUNCTION update_total_amount_paid()
        RETURNS TRIGGER AS $$
        BEGIN
            UPDATE loan
            SET total_amount_paid = total_amount_paid + NEW.amount_to_be_paid
            WHERE id = NEW.loan_id;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        """))

    

    pass


def downgrade() -> None:
    op.execute(text("""
        DROP FUNCTION update_total_amount_paid();
        """))
    pass
