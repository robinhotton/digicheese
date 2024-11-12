from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.services.client_service import ClientService

router = APIRouter(prefix="/clients", tags=["Clients"])

class ClientRouter:
    def __init__(self, client_service: ClientService):
        self.service = client_service
        

    @router.get("/", response_model=list)
    def read_clients(self, db: Session = Depends(get_db)):
        return self.service.list_clients(db)


    @router.get("/{client_id}", response_model=dict)
    def read_client(self, client_id: int, db: Session = Depends(get_db)):
        try:
            return self.service.fetch_client_by_id(db, client_id)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))


    @router.post("/", response_model=dict)
    def create_client(self, client_data: dict, db: Session = Depends(get_db)):
        return self.service.add_client(db, client_data)


    @router.put("/{client_id}", response_model=dict)
    def update_client(self, client_id: int, client_data: dict, db: Session = Depends(get_db)):
        client = self.service.read_client(client_id, db)
        if not client:
            self.service.create_client(client_data, db)
        else:
            self.service.update_client(client_data)
        return client


    @router.delete("/{client_id}", response_model=dict)
    def delete_client(self, client_id: int, db: Session = Depends(get_db)):
        client = self.service.remove_client(db, client_id)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return client
