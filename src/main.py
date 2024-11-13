from fastapi import FastAPI
from .database import engine
from .models import *
from .routers import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)