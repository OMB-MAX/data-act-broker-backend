"""addOriginalFilenames

Revision ID: cdb714f6f374
Revises: 37bf5b71b83f
Create Date: 2016-03-22 16:07:16.229000

"""

# revision identifiers, used by Alembic.
revision = 'cdb714f6f374'
down_revision = '37bf5b71b83f'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('error_data', 'field_name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('error_data', 'first_row',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('error_data', 'job_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('error_data', 'occurrences',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('error_type', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('error_type', 'name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('file_status', 'status_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('status', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('status', 'name',
               existing_type=sa.TEXT(),
               nullable=True)
    ### end Alembic commands ###


def downgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('status', 'name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('status', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('file_status', 'status_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('error_type', 'name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('error_type', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('error_data', 'occurrences',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('error_data', 'job_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('error_data', 'first_row',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('error_data', 'field_name',
               existing_type=sa.TEXT(),
               nullable=False)
    ### end Alembic commands ###


def upgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('job_dependency', 'job_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('job_dependency', 'prerequisite_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('job_status', sa.Column('original_filename', sa.Text(), nullable=True))
    op.alter_column('job_status', 'status_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('job_status', 'submission_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('job_status', 'type_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('resource', 'ip')
    op.alter_column('status', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('status', 'name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('type', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('type', 'name',
               existing_type=sa.TEXT(),
               nullable=True)
    ### end Alembic commands ###


def downgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('type', 'name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('type', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('status', 'name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('status', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    op.add_column('resource', sa.Column('ip', sa.TEXT(), autoincrement=False, nullable=False))
    op.alter_column('job_status', 'type_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('job_status', 'submission_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('job_status', 'status_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('job_status', 'original_filename')
    op.alter_column('job_dependency', 'prerequisite_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('job_dependency', 'job_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    ### end Alembic commands ###


# def upgrade_user_manager():
    ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('email_template')
    # op.drop_table('email_template_type')
    # op.drop_table('email_token')
    ### end Alembic commands ###


# def downgrade_user_manager():
#     ### commands auto generated by Alembic - please adjust! ###
#     op.create_table('email_token',
#     sa.Column('email_token_id', sa.INTEGER(), server_default=sa.text(u"nextval('emailtokenserial'::regclass)"), nullable=False),
#     sa.Column('token', sa.TEXT(), autoincrement=False, nullable=True),
#     sa.Column('salt', sa.TEXT(), autoincrement=False, nullable=True),
#     sa.PrimaryKeyConstraint('email_token_id', name=u'email_token_pkey')
#     )
#     op.create_table('email_template_type',
#     sa.Column('email_template_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
#     sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
#     sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
#     sa.PrimaryKeyConstraint('email_template_type_id', name=u'email_template_type_pkey')
#     )
#     op.create_table('email_template',
#     sa.Column('email_template_id', sa.INTEGER(), server_default=sa.text(u"nextval('emailtemplateserial'::regclass)"), nullable=False),
#     sa.Column('subject', sa.TEXT(), autoincrement=False, nullable=True),
#     sa.Column('content', sa.TEXT(), autoincrement=False, nullable=True),
#     sa.Column('template_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
#     sa.PrimaryKeyConstraint('email_template_id', name=u'email_template_pkey')
#     )
    ### end Alembic commands ###

