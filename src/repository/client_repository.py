from sqlalchemy.orm import Session
from ..models import Client
from ..schemas import ClientCreate, ClientUpdate


class ClientRepository:

    def get_all_clients(self, db: Session):
        return db.query(Client).all()


    def get_client_by_id(self, db: Session, client_id: int):
        return db.query(Client).filter(Client.codcli == client_id).first()


    def create_client(self, db: Session, client_data: ClientCreate):
        new_client = Client(**client_data.model_dump())
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
        return new_client


    def update_client(self, db: Session, client_id: int, client_data: ClientUpdate):
        client_data = client_data.model_dump(exclude_unset=True)
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
