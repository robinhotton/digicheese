from pydantic import BaseModel
from typing import Optional


class ClientBase(BaseModel):
	nomcli: Optional[str]
	prenomcli: Optional[str]
	genrecli: Optional[str]
	adresse1cli: Optional[str]
	adresse2cli: Optional[str]
	adresse3cli: Optional[str]
	telcli: Optional[str]
	emailcli: Optional[str]
	portcli: Optional[str]
	newsletter: Optional[int]


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientBase):
    pass


class Client(ClientBase):
    codcli: int

    class Config:
        from_attributes = True