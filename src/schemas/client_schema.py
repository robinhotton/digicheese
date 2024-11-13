from pydantic import BaseModel
from typing import Optional


class ClientBase(BaseModel):
	nomcli: Optional[str] = None
	prenomcli: Optional[str] = None
	genrecli: Optional[str] = None
	adresse1cli: Optional[str] = None
	adresse2cli: Optional[str] = None
	adresse3cli: Optional[str] = None
	telcli: Optional[str] = None
	emailcli: Optional[str] = None
	portcli: Optional[str] = None
	newsletter: Optional[int] = None


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientBase):
    pass


class Client(ClientBase):
    codcli: int

    class Config:
        from_attributes = True