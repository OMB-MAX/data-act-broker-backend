"""rulesetting and ruleimpact tables

Revision ID: 244959349467
Revises: 9e58ce58e4ee
Create Date: 2020-02-04 13:18:13.234795

"""

# revision identifiers, used by Alembic.
revision = '244959349467'
down_revision = 'e24af362f06a'
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
    op.create_table('rule_impact',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('rule_impact_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Text(), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint('rule_impact_id')
    )
    op.create_table('rule_settings',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('rule_settings_id', sa.Integer(), nullable=False),
        sa.Column('agency_code', sa.Text(), nullable=True),
        sa.Column('rule_id', sa.Integer(), nullable=False),
        sa.Column('priority', sa.Integer(), nullable=False),
        sa.Column('impact_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['rule_id'], ['rule_sql.rule_sql_id'], name='fk_rule'),
        sa.ForeignKeyConstraint(['impact_id'], ['rule_impact.rule_impact_id'], name='fk_impact'),
        sa.PrimaryKeyConstraint('rule_settings_id')
    )
    # ### end Alembic commands ###


def downgrade_data_broker():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rule_settings')
    op.drop_table('rule_impact')
    # ### end Alembic commands ###

