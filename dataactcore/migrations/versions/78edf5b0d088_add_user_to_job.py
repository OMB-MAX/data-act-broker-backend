"""add user to job

Revision ID: 78edf5b0d088
Revises: 23f213c103cf
Create Date: 2016-12-06 11:57:54.599715

"""

# revision identifiers, used by Alembic.
revision = '78edf5b0d088'
down_revision = '23f213c103cf'
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
    op.add_column('job', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_job_user', 'job', 'users', ['user_id'], ['user_id'], ondelete='SET NULL')
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_job_user', 'job', type_='foreignkey')
    op.drop_column('job', 'user_id')
    ### end Alembic commands ###
