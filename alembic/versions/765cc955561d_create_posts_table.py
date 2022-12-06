"""create posts table

Revision ID: 765cc955561d
Revises: 
Create Date: 2022-12-04 18:08:31.890786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '765cc955561d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
