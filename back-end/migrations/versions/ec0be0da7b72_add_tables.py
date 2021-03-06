"""add tables

Revision ID: ec0be0da7b72
Revises: 
Create Date: 2020-06-05 12:04:03.669631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec0be0da7b72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('name_zh', sa.String(length=128), nullable=True),
    sa.Column('icon_cls', sa.String(length=128), nullable=True),
    sa.Column('component', sa.String(length=128), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('path')
    )
    op.create_table('admin_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('name_zh', sa.String(length=128), nullable=True),
    sa.Column('enabled', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_role_menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rid', sa.Integer(), nullable=True),
    sa.Column('mid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('admin_user_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('rid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('article_title', sa.String(length=128), nullable=False),
    sa.Column('article_content_md', sa.Text(), nullable=True),
    sa.Column('article_content_html', sa.Text(), nullable=True),
    sa.Column('article_abstract', sa.String(length=128), nullable=True),
    sa.Column('article_cover', sa.String(length=128), nullable=True),
    sa.Column('article_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('no', sa.Float(), nullable=True),
    sa.Column('abbr', sa.String(length=128), nullable=True),
    sa.Column('tag', sa.String(length=128), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('subtitle', sa.String(length=128), nullable=True),
    sa.Column('author', sa.String(length=128), nullable=True),
    sa.Column('compile', sa.String(length=128), nullable=True),
    sa.Column('interpreter', sa.String(length=128), nullable=True),
    sa.Column('publish_date', sa.DateTime(), nullable=True),
    sa.Column('overprint_date', sa.String(length=128), nullable=True),
    sa.Column('num_of_volumes', sa.String(length=128), nullable=True),
    sa.Column('language', sa.String(length=128), nullable=True),
    sa.Column('binding_style', sa.String(length=128), nullable=True),
    sa.Column('size', sa.String(length=128), nullable=True),
    sa.Column('num_of_pages', sa.Integer(), nullable=True),
    sa.Column('num_of_bw_images', sa.Integer(), nullable=True),
    sa.Column('num_of_color_images', sa.Integer(), nullable=True),
    sa.Column('ISBN', sa.String(length=128), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('abstract', sa.Text(), nullable=True),
    sa.Column('info_of_author', sa.Text(), nullable=True),
    sa.Column('remark', sa.String(length=128), nullable=True),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('category')
    op.drop_table('book')
    op.drop_table('article')
    op.drop_table('admin_user_role')
    op.drop_table('admin_role_menu')
    op.drop_table('admin_role')
    op.drop_table('admin_menu')
    # ### end Alembic commands ###
