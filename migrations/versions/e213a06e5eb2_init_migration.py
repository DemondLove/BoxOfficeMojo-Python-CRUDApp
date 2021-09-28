"""init migration

Revision ID: e213a06e5eb2
Revises: 
Create Date: 2021-09-27 18:06:03.215532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e213a06e5eb2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('title',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_title_title'), 'title', ['title'], unique=True)

    op.execute('''INSERT INTO title
        (title)
        VALUES
            ('Following'),
            ('Memento'),
            ('Insomnia'),
            ('Batman Begins'),
            ('The Prestige'),
            ('The Dark Knight'),
            ('Inception'),
            ('The Dark Knight Rises'),
            ('Interstellar'),
            ('Dunkirk'),
            ('Tenet')
    ''')


def downgrade():
    op.drop_index(op.f('ix_title_title'), table_name='title')
    op.drop_table('title')
