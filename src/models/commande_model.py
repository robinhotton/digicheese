from src.models.base_model import Base
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Index


class Commande(Base):
	__tablename__ = "t_commande"

	codcde = Column(Integer,primary_key=True)
	datcde = Column(Date)
	codcli = Column(Integer, ForeignKey('t_client.codcli'))
	timbrecli = Column(Float)
	timbrecde = Column(Float)
	cheqcli = Column(Float)
	cdeComt = Column(String(255), default=None)

	__table_args__ = (Index('commmande_index', "cdeComt", "codcli"),)