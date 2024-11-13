from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services import ClientService
from ..schemas import Client, ClientCreate, ClientUpdate


router = APIRouter(prefix="/clients", tags=["Clients"])
service = ClientService()
        

@router.get("/", response_model=List[Client])
def read_clients(db: Session = Depends(get_db)):
    return service.list_clients(db)


@router.get("/{client_id}", response_model=Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    try:
        return service.fetch_client_by_id(db, client_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=Client)
def create_client(client_data: ClientCreate, db: Session = Depends(get_db)):
    return service.add_client(db, client_data)


@router.put("/{client_id}", response_model=Client)
def update_client(client_id: int, client_data: ClientUpdate, db: Session = Depends(get_db)):
    client = service.fetch_client_by_id(db, client_id)
    if not client:
        service.add_client(db, client_data)
    else:
        service.update_client(db, client_id, client_data)
        return client


@router.delete("/{client_id}", response_model=Client)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = service.remove_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client
