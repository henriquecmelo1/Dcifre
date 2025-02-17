from pydantic import BaseModel

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int
    class Config:
        from_attributes = True
        



# Empresa (Empresa):
# id: int (PK)
# nome: str
# cnpj: str (único)
# endereco: str
# email: str
# telefone: str