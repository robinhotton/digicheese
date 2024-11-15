from pydantic import BaseModel, EmailStr, Field, StringConstraints
from typing import Optional, Annotated


class ClientBase(BaseModel):
    nom: Optional[Annotated[str, StringConstraints(min_length=1, max_length=40)]] = None
    prenom: Optional[Annotated[str, StringConstraints(min_length=1, max_length=30)]] = None
    genre: Optional[Annotated[str, StringConstraints(max_length=8)]] = None
    adresse_ligne1: Optional[Annotated[str, StringConstraints(max_length=50)]] = None
    adresse_ligne2: Optional[Annotated[str, StringConstraints(max_length=50)]] = None
    adresse_complement: Optional[Annotated[str, StringConstraints(max_length=50)]] = None
    tel: Optional[Annotated[str, StringConstraints(pattern=r'^\d{10}$')]] = None # Numéro de téléphone valide (exactement 10 chiffres)
    email: Optional[EmailStr] = None # Validation du format d'email
    newsletter: Optional[bool] = Field(0, ge=0, le=1) # Newsletter doit être 0 ou 1

    class Config:
        from_attributes = True  


class ClientCreate(ClientBase):
    # Nom et prénom requis lors de la création
    nom: Annotated[str, StringConstraints(min_length=1, max_length=40)]
    prenom: Annotated[str, StringConstraints(min_length=1, max_length=30)]


class ClientUpdate(ClientBase):
    pass


class Client(ClientBase):
    client_id: int  # Identifiant client obligatoire

    class Config:
        from_attributes = True  # Permet l'initialisation à partir des objets ORM
