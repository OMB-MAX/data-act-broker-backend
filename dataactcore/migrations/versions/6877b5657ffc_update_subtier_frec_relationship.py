"""update subtier-frec relationship

Revision ID: 6877b5657ffc
Revises: 6fc9bcd1c6cd
Create Date: 2017-08-21 14:57:32.560466

"""

# revision identifiers, used by Alembic.
revision = '6877b5657ffc'
down_revision = '6fc9bcd1c6cd'
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
    op.add_column('frec', sa.Column('cgac_id', sa.Integer(), nullable=True))
    op.execute("""
                UPDATE frec
                SET cgac_id = cgacs.cgac_id
                FROM (
                    SELECT cgac_id, cgac_code
                    FROM cgac) cgacs
                WHERE cgacs.cgac_code = frec.cgac_code
            """)
    op.alter_column('frec', 'cgac_id', existing_type=sa.INTEGER(), nullable=False)
    op.create_foreign_key('fk_frec_cgac', 'frec', 'cgac', ['cgac_id'], ['cgac_id'], ondelete='CASCADE')
    op.drop_column('frec', 'cgac_code')
    op.add_column('sub_tier_agency', sa.Column('frec_id', sa.Integer(), nullable=True))
    op.add_column('sub_tier_agency', sa.Column('is_frec', sa.Boolean(), server_default='False', nullable=False))
    op.create_foreign_key('fk_sub_tier_agency_frec', 'sub_tier_agency', 'frec', ['frec_id'], ['frec_id'], ondelete='CASCADE')
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_sub_tier_agency_frec', 'sub_tier_agency', type_='foreignkey')
    op.drop_column('sub_tier_agency', 'is_frec')
    op.drop_column('sub_tier_agency', 'frec_id')
    op.add_column('frec', sa.Column('cgac_code', sa.TEXT(), autoincrement=False, nullable=True))
    op.execute("""
                UPDATE frec
                SET cgac_code = cgacs.cgac_code
                FROM (
                    SELECT cgac_id, cgac_code
                    FROM cgac) cgacs
                WHERE cgacs.cgac_id = frec.cgac_id
            """)
    op.drop_constraint('fk_frec_cgac', 'frec', type_='foreignkey')
    op.drop_column('frec', 'cgac_id')
    ### end Alembic commands ###
