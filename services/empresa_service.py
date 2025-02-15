from sqlalchemy.orm import Session
from models.empresa_model import Empresa

def create_empresa(db: Session, empresa: Empresa):
    db_empresa = Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def get_empresas(db: Session):
    return db.query(Empresa).all()

def get_empresa(db: Session, empresa_id: int):
    return db.query(Empresa).filter(Empresa.id == empresa_id).first()

def update_empresa(db: Session, empresa_id: int, empresa: Empresa):
    db.query(Empresa).filter(Empresa.id == empresa_id).update(empresa.dict())
    db.commit()
    return db.query(Empresa).filter(Empresa.id == empresa_id).first()

def delete_empresa(db: Session, empresa_id: int):
    db.query(Empresa).filter(Empresa.id == empresa_id).delete()
    db.commit()
    return "Empresa removida"