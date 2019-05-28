"""Add high comp officer fields to published_award_financial_assistance table

Revision ID: ad3dd1c0cf20
Revises: 5f29b283f23e
Create Date: 2019-05-23 08:31:35.225654

"""

# revision identifiers, used by Alembic.
revision = 'ad3dd1c0cf20'
down_revision = '5f29b283f23e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('published_award_financial_assistance', sa.Column('high_comp_officer1_amount', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('high_comp_officer1_full_na', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('high_comp_officer2_amount', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('high_comp_officer2_full_na', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('high_comp_officer3_amount', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('high_comp_officer3_full_na', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('high_comp_officer4_amount', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('high_comp_officer4_full_na', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('high_comp_officer5_amount', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('high_comp_officer5_full_na', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade_data_broker():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('published_award_financial_assistance', 'high_comp_officer5_full_na')
    op.drop_column('published_award_financial_assistance', 'high_comp_officer5_amount')
    op.drop_column('published_award_financial_assistance', 'high_comp_officer4_full_na')
    op.drop_column('published_award_financial_assistance', 'high_comp_officer4_amount')
    op.drop_column('published_award_financial_assistance', 'high_comp_officer3_full_na')
    op.drop_column('published_award_financial_assistance', 'high_comp_officer3_amount')
    op.drop_column('published_award_financial_assistance', 'high_comp_officer2_full_na')
    op.drop_column('published_award_financial_assistance', 'high_comp_officer2_amount')
    op.drop_column('published_award_financial_assistance', 'high_comp_officer1_full_na')
    op.drop_column('published_award_financial_assistance', 'high_comp_officer1_amount')
    # ### end Alembic commands ###

