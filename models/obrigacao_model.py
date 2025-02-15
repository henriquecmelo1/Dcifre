from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Obrigacao(Base):
    __tablename__ = "obrigacoes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    periodicidade = Column(String)
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
