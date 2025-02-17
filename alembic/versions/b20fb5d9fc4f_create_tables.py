"""create tables

Revision ID: b20fb5d9fc4f
Revises: 
Create Date: 2025-02-16 22:28:35.862746

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b20fb5d9fc4f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('empresas',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('empresas_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cnpj', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('endereco', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('telefone', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='empresas_pkey'),
    sa.UniqueConstraint('cnpj', name='empresas_cnpj_key'),
    postgresql_ignore_search_path=False
    )

    op.create_index('ix_empresas_id', 'empresas', ['id'], unique=False) #index para evitar full table scan e unique = False pois id já é PK

    op.create_table('obrigacoes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('periodicidade', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('empresa_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['empresa_id'], ['empresas.id'], name='obrigacoes_empresa_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='obrigacoes_pkey')
    )
    op.create_index('ix_obrigacoes_id', 'obrigacoes', ['id'], unique=False) #index para evitar full table scan e unique = False pois id já é PK



def downgrade() -> None:
    op.drop_index('ix_obrigacoes_id', table_name='obrigacoes')
    op.drop_table('obrigacoes')
    op.drop_index('ix_empresas_id', table_name='empresas')
    op.drop_table('empresas')