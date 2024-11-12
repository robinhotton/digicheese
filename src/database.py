from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import connection_string

# url de connexion de la base
SQLALCHEMY_DATABASE_URL = connection_string()

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