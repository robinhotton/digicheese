from src.models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Detail(Base):
	__tablename__ = "t_detail_commande"

	id = Column(Integer,primary_key=True)
	codcde = Column(Integer,ForeignKey('t_commande.codcde'), index=True)
	qte = Column(Integer, default=1)
	commentaire = Column(String(100), default=None)