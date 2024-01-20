"""add content column to post table

Revision ID: 24cf9ffe3e57
Revises: 45ecc3a8c7ab
Create Date: 2024-01-20 15:57:32.120465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24cf9ffe3e57'
down_revision: Union[str, None] = '45ecc3a8c7ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.add_column('posts' , sa.Column('content' , sa.String, nullable=False),)
    pass


def downgrade() :
    op.drop_column('posts' ,'content')
    pass
