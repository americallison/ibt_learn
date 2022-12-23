"""added info image

Revision ID: 2258d5919d84
Revises: 67e94a0dce62
Create Date: 2022-11-19 13:50:52.593160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2258d5919d84'
down_revision = '67e94a0dce62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('information', schema=None) as batch_op:
        batch_op.add_column(sa.Column('info_image', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('information', schema=None) as batch_op:
        batch_op.drop_column('info_image')

    # ### end Alembic commands ###