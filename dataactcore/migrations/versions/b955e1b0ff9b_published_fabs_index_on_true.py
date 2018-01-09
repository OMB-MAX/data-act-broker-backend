"""published fabs index on true

Revision ID: b955e1b0ff9b
Revises: 605bcaf99c01
Create Date: 2018-01-09 09:30:56.615501

"""

# revision identifiers, used by Alembic.
revision = 'b955e1b0ff9b'
down_revision = '605bcaf99c01'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_published_award_financial_assistance_is_active', 'published_award_financial_assistance', ['is_active'], unique=False, postgresql_where=sa.text('is_active = true'))
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_published_award_financial_assistance_is_active', table_name='published_award_financial_assistance')
    ### end Alembic commands ###

