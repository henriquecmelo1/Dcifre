from fastapi import APIRouter, Depends
from obrigacao_service import create_obrigacao, get_obrigacoes, get_obrigacao, update_obrigacao, delete_obrigacao
from database import get_db
from sqlalchemy.orm import Session
from obrigacao_schema import ObrigacaoBase, Obrigacao

router = APIRouter(tags=["Obrigações"], prefix='/obrigacoes')

@router.post("/")
async def create_obrigacao_route(obrigacao: ObrigacaoBase, db: Session = Depends(get_db)):
    return create_obrigacao(db=db, obrigacao=obrigacao)

@router.get("/")
async def get_obrigacoes_route(db: Session = Depends(get_db)):
    return get_obrigacoes(db=db)

@router.get("/{obrigacao_id}")
async def get_obrigacao_route(obrigacao_id: int, db: Session = Depends(get_db)):
    return get_obrigacao(db=db, obrigacao_id=obrigacao_id)

@router.put("/{obrigacao_id}")
async def update_obrigacao_route(obrigacao_id: int, obrigacao: ObrigacaoBase, db: Session = Depends(get_db)):
    return update_obrigacao(db=db, obrigacao_id=obrigacao_id, obrigacao=obrigacao)

@router.delete("/{obrigacao_id}")
async def delete_obrigacao_route(obrigacao_id: int, db: Session = Depends(get_db)):
    return delete_obrigacao(db=db, obrigacao_id=obrigacao_id)

