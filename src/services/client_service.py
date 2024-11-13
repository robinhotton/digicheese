from sqlalchemy.orm import Session
from ..repository import ClientRepository
from ..schemas import ClientCreate, ClientUpdate


class ClientService:
    repository = ClientRepository()


    def fetch_client_by_id(self, db: Session, client_id: int):
        client = self.repository.get_client_by_id(db, client_id)
        if not client:
            raise ValueError("Client not found")
        return client


    def list_clients(self, db: Session):
        return self.repository.get_all_clients(db)


    def add_client(self, db: Session, client_data: ClientCreate):
        return self.repository.create_client(db, client_data)


    def update_client(self, db: Session, client_id: int, client_data: ClientUpdate):
        updated_client = self.repository.update_client(db, client_id, client_data)
        if not updated_client:
            raise ValueError("Client not found for update")
        return updated_client


    def remove_client(self, db: Session, client_id: int):
        client = self.repository.delete_client(db, client_id)
        if not client:
            raise ValueError("Client not found for deletion")
        return client
    