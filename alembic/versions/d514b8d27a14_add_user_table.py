"""add user table

Revision ID: d514b8d27a14
Revises: 5dec84372f27
Create Date: 2026-10-17 12:32:41.047134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd514b8d27a14'
down_revision: Union[str, Sequence[str], None] = '5dec84372f27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), 
                             sa.Column('email', sa.String(), nullable=False), 
                             sa.Column('password', sa.String(), nullable=False), 
                             sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                             sa.PrimaryKeyConstraint('id'),
                             sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
