"""add user table

Revision ID: f91daa3cf59b
Revises: 24cf9ffe3e57
Create Date: 2024-01-20 16:03:40.289536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f91daa3cf59b'
down_revision: Union[str, None] = '24cf9ffe3e57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.create_table('users',
              sa.Column('id' , sa.Integer(),nullable=False),
              sa.Column('email',sa.String(),nullable=False),
              sa.Column('password',sa.String(),nullable=False),
              sa.Column('created_at',sa.TIMESTAMP(timezone=False),
                        server_default=sa.text('now()'),nullable=False),
              sa.PrimaryKeyConstraint('id'),
              sa.UniqueConstraint('email'),

             )
    pass


def downgrade() :
    op.drop_table('users')
    pass
