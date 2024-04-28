"""Adding views , last one was used for other purpose

Revision ID: 2cb1d13d632b
Revises: 4d7c6245147d
Create Date: 2024-04-27 14:15:02.492379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision: str = '2cb1d13d632b'
down_revision: Union[str, None] = '4d7c6245147d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade()->None:
    op.alter_column('employee_details','Name',new_column_name='name')
    op.alter_column('employee_details', 'Salary', new_column_name='salary')   