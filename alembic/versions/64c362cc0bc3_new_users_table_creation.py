"""new users table creation

Revision ID: 64c362cc0bc3
Revises: f91daa3cf59b
Create Date: 2024-01-20 16:51:45.983231

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64c362cc0bc3'
down_revision: Union[str, None] = 'f91daa3cf59b'
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
