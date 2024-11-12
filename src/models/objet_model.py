from src.models.base_model import Base
from sqlalchemy import Column, Integer, String, Numeric


class Objet(Base):
	__tablename__ = "t_objet"

	codobj = Column(Integer,primary_key=True)
	libobj = Column(String(50), default=None)
	tailleobj = Column(String(50), default=None)
	puobj = Column(Numeric, default=0.0000)
	poidsobj = Column(Numeric, default=0.0000)
	points = Column(Integer, default=0)