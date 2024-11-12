from src.models.base_model import Base
from sqlalchemy import Column, Integer, String


class Client(Base):
	__tablename__ = "t_client"

	codcli = Column(Integer,primary_key=True)
	genrecli = Column(String(8), default=None)
	nomcli = Column(String(40), default=None, index=True)
	prenomcli = Column(String(30), default=None)
	adresse1cli = Column(String(50), default=None)
	adresse2cli = Column(String(50), default=None)
	adresse3cli = Column(String(50), default=None)
	telcli = Column(String(10), default=None)
	emailcli = Column(String(255), default=None)
	portcli = Column(String(10), default=None)
	newsletter = Column(Integer, default=0)