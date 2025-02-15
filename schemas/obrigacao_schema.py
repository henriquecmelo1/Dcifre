from pydantic import BaseModel

class ObrigacaoBase(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

class ObrigacaoCreate(ObrigacaoBase):
    pass

class Obrigacao(ObrigacaoBase):
    id: int
    class Config:
        from_attributes = True



# Obrigação Acessória (ObrigacaoAcessoria):
# id: int (PK)
# nome: str
# periodicidade: str (mensal, trimestral, anual)
# empresa_id: int (FK -> Empresa)