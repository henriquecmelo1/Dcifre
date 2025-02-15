from fastapi import FastAPI
from routers.empresa_router import router as router_e
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_e)
