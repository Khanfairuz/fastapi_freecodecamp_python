"""add last few columns to posts table 

Revision ID: cb1d85e14423
Revises: 4427885d3c84
Create Date: 2024-01-20 17:00:43.476421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb1d85e14423'
down_revision: Union[str, None] = '4427885d3c84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.add_column('posts',sa.Column('published', sa.Boolean(),nullable=False,server_default="TRUE"),)
    op.add_column('posts' , sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')),)
    pass


def downgrade() :
    op.drop_column('posts' ,'published')
    op.drop_column('posts','created_at')
    pass
