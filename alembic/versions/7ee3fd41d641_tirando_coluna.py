"""tirando coluna

Revision ID: 7ee3fd41d641
Revises: ff57dabadfac
Create Date: 2023-04-06 11:16:59.723832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ee3fd41d641'
down_revision = 'ff57dabadfac'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('filmes', 'bilheteria')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('filmes', sa.Column('bilheteria', sa.FLOAT(), nullable=True))
    # ### end Alembic commands ###
