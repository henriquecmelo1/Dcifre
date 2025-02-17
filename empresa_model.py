from sqlalchemy import Column, Integer, String
from database import Base

class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cnpj = Column(String, unique=True)
    endereco = Column(String)
    email = Column(String)
    telefone = Column(String)

