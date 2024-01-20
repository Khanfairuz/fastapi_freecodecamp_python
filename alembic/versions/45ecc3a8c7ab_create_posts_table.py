"""Create posts table

Revision ID: 45ecc3a8c7ab
Revises: 
Create Date: 2024-01-20 14:05:57.694048

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45ecc3a8c7ab'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


#all the logics to create posts table
def upgrade() :
      op.create_table('posts',sa.Column('id', sa.INTEGER(),nullable=False,primary_key=True) ,sa.Column('tottle',sa.String(),nullable=False)),
      pass


#to roll bcak changes
def downgrade() :
    op.drop_table('posts')

    pass
