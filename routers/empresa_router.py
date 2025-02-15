from fastapi import APIRouter, Depends
from services.empresa_service import create_empresa, get_empresas, get_empresa, update_empresa, delete_empresa 
from database import get_db
from sqlalchemy.orm import Session
from schemas.empresa_schema import EmpresaBase, Empresa

router = APIRouter()

@router.post("/empresas")
async def create_empresa_route(empresa: EmpresaBase, db: Session = Depends(get_db)):
    return create_empresa(db=db, empresa=empresa)

@router.get("/empresas")
async def get_empresas_route(db: Session = Depends(get_db)):
    return get_empresas(db=db)

@router.get("/empresas/{empresa_id}")
async def get_empresa_route(empresa_id: int, db: Session = Depends(get_db)):
    return get_empresa(db=db, empresa_id=empresa_id)

@router.put("/empresas/{empresa_id}")
async def update_empresa_route(empresa_id: int, empresa: EmpresaBase, db: Session = Depends(get_db)):
    return update_empresa(db=db, empresa_id=empresa_id, empresa=empresa)

@router.delete("/empresas/{empresa_id}")
async def delete_empresa_route(empresa_id: int, db: Session = Depends(get_db)):
    return delete_empresa(db=db, empresa_id=empresa_id)


