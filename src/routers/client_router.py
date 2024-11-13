from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..services import ClientService

router = APIRouter(prefix="/clients", tags=["Clients"])
service = ClientService()
        

@router.get("/", response_model=list)
def read_clients( db: Session = Depends(get_db)):
    return service.list_clients(db)


@router.get("/{client_id}", response_model=dict)
def read_client( client_id: int, db: Session = Depends(get_db)):
    try:
        return service.fetch_client_by_id(db, client_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=dict)
def create_client( client_data: dict, db: Session = Depends(get_db)):
    return service.add_client(db, client_data)


@router.put("/{client_id}", response_model=dict)
def update_client( client_id: int, client_data: dict, db: Session = Depends(get_db)):
    client = service.read_client(client_id, db)
    if not client:
        service.create_client(client_data, db)
    else:
        service.update_client(client_data)
        return client


@router.delete("/{client_id}", response_model=dict)
def delete_client( client_id: int, db: Session = Depends(get_db)):
    client = service.remove_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client
