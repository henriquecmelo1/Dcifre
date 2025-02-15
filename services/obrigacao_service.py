from sqlalchemy.orm import Session
from models.obrigacao_model import Obrigacao

def create_obrigacao(db: Session, obrigacao: Obrigacao):
    db_obrigacao = Obrigacao(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

def get_obrigacoes(db: Session):
    return db.query(Obrigacao).all()

def get_obrigacao(db: Session, obrigacao_id: int):
    return db.query(Obrigacao).filter(Obrigacao.id == obrigacao_id).first()

def update_obrigacao(db: Session, obrigacao_id: int, obrigacao: Obrigacao):
    db.query(Obrigacao).filter(Obrigacao.id == obrigacao_id).update(obrigacao.dict())
    db.commit()
    return db.query(Obrigacao).filter(Obrigacao.id == obrigacao_id).first()

def delete_obrigacao(db: Session, obrigacao_id: int):
    db.query(Obrigacao).filter(Obrigacao.id == obrigacao_id).delete()
    db.commit()
    return "Obrigação removida"