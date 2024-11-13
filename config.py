import os

# variables d'environnement pour la connexion à la base de données
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# Configuration de la connexion à la base de données
connector = os.getenv("DB_CONNECTOR", "mysql+pymysql")  # mysql+pymysql par défaut
host = os.getenv("DB_HOST", "localhost")                # localhost par défaut

# Chaine de connexion de la base de données
def connection_string():
    return f"{connector}://{username}:{password}@{host}/{database}"