import os

connector = os.getenv("DB_CONNECTOR", "mysql+pymysql")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST", "localhost")
database = os.getenv("DB_NAME")

# connexion à la base de données
def connection_string():
    return f"{connector}://{username}:{password}@{host}/{database}"