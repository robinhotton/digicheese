from fastapi import FastAPI
from src.routers import client_router
from src.database import engine
from src.models.base_model import Base
from src.models.client_model import Client
from src.models.commande_model import Commande
from src.models.detail_model import Detail
from src.models.objet_model import Objet

Base.metadata.create_all(bind=engine)

app = FastAPI(prefix="/api/v1")

# Inclure le routeur pour l'entité Client
app.include_router(client_router.router)