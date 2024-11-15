from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# variables d'environnement pour la connexion à la base de données
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# Configuration de la connexion à la base de données
connector = os.getenv("DB_CONNECTOR", "mysql+pymysql")  # mysql+pymysql par défaut
host = os.getenv("DB_HOST", "localhost")                # localhost par défaut

# url de connexion de la base
SQLALCHEMY_DATABASE_URL = f"{connector}://{username}:{password}@{host}/{database}"

# permet de définir les paramètre de connexion à la base
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# creation d'une session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    """Maintenir la connexion ouverte pour toute la durée de la requête"""
    db = SessionLocal()
    try:
        yield db # couplé avec Depends de fastapi
    finally:
        db.close() # fermeture de la session