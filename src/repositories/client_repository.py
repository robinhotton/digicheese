from sqlalchemy.orm import Session
from ..models import Client


class ClientRepository:
    def get_all_clients(self, db: Session):
        return db.query(Client).all()


    def get_client_by_id(self, db: Session, client_id: int):
        return db.query(Client).filter(Client.client_id == client_id).first()
    
    
    def get_client_by_email(self, db: Session, email: str):
        return db.query(Client).filter(Client.email == email).first()
    
    
    def get_client_by_name(self, db: Session, nom: str, prenom: str):
        return db.query(Client).filter(Client.nom == nom, Client.prenom == prenom).first()


    def create_client(self, db: Session, client_data: dict):
        new_client = Client(**client_data)
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
        return new_client


    def update_client(self, db: Session, client_id: int, client_data: dict):
        client = self.get_client_by_id(db, client_id)
        
        if client:
            for key, value in client_data.items():
                setattr(client, key, value)
            db.commit()
            db.refresh(client)
            return client
        return None


    def delete_client(self, db: Session, client_id: int):
        client = self.get_client_by_id(db, client_id)
        if client:
            db.delete(client)
            db.commit()
            return client
        return None
