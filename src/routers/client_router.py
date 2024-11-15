from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services import ClientService
from ..schemas import Client, ClientCreate, ClientUpdate


router = APIRouter()
service = ClientService()
        

@router.get("/", response_model=List[Client])
def get_all_clients(db: Session = Depends(get_db)):
    return service.fetch_all_clients(db)


@router.get("/{client_id}", response_model=Client)
def get_client_by_id(client_id: int, db: Session = Depends(get_db)):
    try:
        return service.fetch_client_by_id(db, client_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/email/{email}", response_model=Client)
def get_client_by_email(email: str, db: Session = Depends(get_db)):
    try:
        return service.fetch_client_by_email(db, email)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.get("/{nom}/{prenom}", response_model=Client)
def get_client_by_name(nom: str, prenom: str, db: Session = Depends(get_db)):
    try:
        return service.fetch_client_by_name(db, nom, prenom)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=Client)
def create_client(client_data: ClientCreate, db: Session = Depends(get_db)):
    return service.add_client(db, client_data)


@router.patch("/{client_id}", response_model=Client)
def patch_client(client_id: int, client_data: ClientUpdate, db: Session = Depends(get_db)):
    client = service.fetch_client_by_id(db, client_id)
    if not client:
        service.add_client(db, client_data)
    else:
        service.patch_client(db, client_id, client_data)
        return client


@router.delete("/{client_id}", response_model=Client)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = service.remove_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client
