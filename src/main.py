from fastapi import FastAPI
from src.database import engine
from src.models import *
from src.routers import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Bienvenue sur notre API DIGICHEESE"}