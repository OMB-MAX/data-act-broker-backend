"""adding territories or freely associated states flag to country code

Revision ID: 1fb19acc7d64
Revises: 0cf297fa927c
Create Date: 2019-04-16 14:32:40.284194

"""

# revision identifiers, used by Alembic.
revision = '1fb19acc7d64'
down_revision = '0cf297fa927c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('country_code', sa.Column('territory_free_state', sa.Boolean(), server_default='False',
                                            nullable=False))
    # ### end Alembic commands ###


def downgrade_data_broker():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('country_code', 'territory_free_state')
    # ### end Alembic commands ###
