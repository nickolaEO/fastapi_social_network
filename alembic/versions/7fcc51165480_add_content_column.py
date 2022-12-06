"""add content column

Revision ID: 7fcc51165480
Revises: 765cc955561d
Create Date: 2022-12-04 18:19:25.689228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fcc51165480'
down_revision = '765cc955561d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
