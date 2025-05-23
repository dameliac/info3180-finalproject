"""empty message

Revision ID: f8788f335f45
Revises: 
Create Date: 2025-05-04 23:20:18.178635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8788f335f45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('photo', sa.String(length=255), nullable=False),
    sa.Column('date_joined', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favourite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_fk', sa.Integer(), nullable=False),
    sa.Column('fav_user_id_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fav_user_id_fk'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id_fk'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_fk', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('parish', sa.String(length=128), nullable=False),
    sa.Column('biography', sa.String(length=255), nullable=False),
    sa.Column('sex', sa.String(length=80), nullable=False),
    sa.Column('race', sa.String(length=128), nullable=False),
    sa.Column('birth_year', sa.Integer(), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('fav_cuisine', sa.String(length=128), nullable=False),
    sa.Column('fav_color', sa.String(length=80), nullable=False),
    sa.Column('fav_school_subject', sa.String(length=80), nullable=False),
    sa.Column('political', sa.Boolean(), nullable=False),
    sa.Column('religious', sa.Boolean(), nullable=False),
    sa.Column('family_oriented', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id_fk'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    op.drop_table('favourite')
    op.drop_table('users')
    # ### end Alembic commands ###
