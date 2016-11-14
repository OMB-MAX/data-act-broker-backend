"""Add dates to tas index

Revision ID: 807a203713a4
Revises: bb33cc8f0a3e
Create Date: 2016-11-09 19:47:52.671178

"""

# revision identifiers, used by Alembic.
revision = '807a203713a4'
down_revision = 'bb33cc8f0a3e'
branch_labels = None
depends_on = None

from alembic import op


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tas', table_name='tas_lookup')
    op.create_index('ix_tas', 'tas_lookup', ['allocation_transfer_agency', 'agency_identifier', 'beginning_period_of_availability', 'ending_period_of_availability', 'availability_type_code', 'main_account_code', 'sub_account_code', 'internal_start_date', 'internal_end_date'], unique=False)
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tas', table_name='tas_lookup')
    op.create_index('ix_tas', 'tas_lookup', ['allocation_transfer_agency', 'agency_identifier', 'beginning_period_of_availability', 'ending_period_of_availability', 'availability_type_code', 'main_account_code', 'sub_account_code'], unique=False)
    ### end Alembic commands ###

