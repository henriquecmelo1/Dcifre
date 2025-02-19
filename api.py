from fastapi import FastAPI
from empresa_router import router as router_e
from obrigacao_router import router as router_o
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_e)
app.include_router(router_o)
