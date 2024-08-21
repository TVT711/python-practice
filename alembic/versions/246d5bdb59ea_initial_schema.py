"""Initial schema

Revision ID: 246d5bdb59ea
Revises: 
Create Date: 2024-04-04 10:49:11.723673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '246d5bdb59ea'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the 'users' table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('username', sa.String, unique=True, index=True),
        sa.Column('first_name', sa.String, nullable=True),
        sa.Column('last_name', sa.String, nullable=True),
        sa.Column('hash_password', sa.String, nullable=False),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('is_admin', sa.Boolean, default=True),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('companies.id'))
    )

    # Create the 'companies' table
    op.create_table(
        'companies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, index=True),
        sa.Column('description', sa.String),
        sa.Column('mode', sa.Integer, nullable=True),
        sa.Column('rating', sa.Integer),
    )

    # Create the 'tasks' table
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('summary', sa.String),
        sa.Column('description', sa.String),
        sa.Column('status', sa.String),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('users.id')),
    )


def downgrade() -> None:
    # Drop the 'tasks' table
    op.drop_table('tasks')

    # Drop the 'companies' table
    op.drop_table('companies')

    # Drop the 'users' table
    op.drop_table('users')
