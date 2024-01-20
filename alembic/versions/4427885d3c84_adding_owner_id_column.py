"""adding owner_id column

Revision ID: 4427885d3c84
Revises: 64c362cc0bc3
Create Date: 2024-01-20 16:54:14.776494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4427885d3c84'
down_revision: Union[str, None] = '64c362cc0bc3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.add_column('posts', sa.Column('owner_id',sa.Integer(), nullable=False))
    op.create_foreign_key('post_ueser_fk' ,source_table="posts",referent_table="users",local_cols=['owner_id'] , remote_cols=['id'] ,ondelete="CASCADE")
    pass


def downgrade() :
    op.drop_constraint('post_ueser_fk' ,table_name='posts')
    op.drop_column('posts' ,'owner_id')
    pass
