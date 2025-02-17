from sqlalchemy.orm import Session
from obrigacao_model import Obrigacao
from fastapi import HTTPException

def create_obrigacao(db: Session, obrigacao: Obrigacao):
    db_obrigacao = Obrigacao(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

def get_obrigacoes(db: Session):
    return db.query(Obrigacao).all()

def get_obrigacao(db: Session, obrigacao_id: int):
    obrigacao =  db.query(Obrigacao).filter(Obrigacao.id == obrigacao_id).first()
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return obrigacao

def update_obrigacao(db: Session, obrigacao_id: int, obrigacao: Obrigacao):
    db.query(Obrigacao).filter(Obrigacao.id == obrigacao_id).update(obrigacao.dict())
    db.commit()
    return db.query(Obrigacao).filter(Obrigacao.id == obrigacao_id).first()

def delete_obrigacao(db: Session, obrigacao_id: int):
    obrigacao = db.query(Obrigacao).filter(Obrigacao.id == obrigacao_id).first()
    if not obrigacao:
        return None
    
    db.delete(obrigacao)
    db.commit()
    return {"message": "Obrigação deletada com sucesso"}