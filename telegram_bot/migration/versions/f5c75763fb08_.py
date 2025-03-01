"""empty message

Revision ID: f5c75763fb08
Revises: 170ce70497bc
Create Date: 2024-05-26 18:26:22.636652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5c75763fb08'
down_revision: Union[str, None] = '170ce70497bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'address', ['id'])
    op.create_unique_constraint(None, 'address_history', ['id'])
    op.create_unique_constraint(None, 'camera_config', ['id'])
    op.create_unique_constraint(None, 'car_number', ['id'])
    op.add_column('car_number_history', sa.Column('car_number_id', sa.INTEGER(), nullable=False))
    op.create_unique_constraint(None, 'car_number_history', ['id'])
    op.create_foreign_key(None, 'car_number_history', 'car_number', ['car_number_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'car_number_history', type_='foreignkey')
    op.drop_constraint(None, 'car_number_history', type_='unique')
    op.drop_column('car_number_history', 'car_number_id')
    op.drop_constraint(None, 'car_number', type_='unique')
    op.drop_constraint(None, 'camera_config', type_='unique')
    op.drop_constraint(None, 'address_history', type_='unique')
    op.drop_constraint(None, 'address', type_='unique')
    # ### end Alembic commands ###
