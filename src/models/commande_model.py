from src.models.base_model import Base
from sqlalchemy import CheckConstraint, Column, Index, Integer, String, Date, Float, ForeignKey
from sqlalchemy.sql import func


class Commande(Base):
    __tablename__ = "t_commande"

	# Clé primaire obligatoire
    commande_id = Column(Integer, primary_key=True)
    
    # Clé étrangère obligatoire
    client_id = Column(Integer, ForeignKey('t_client.client_id', ondelete='CASCADE'), nullable=False)
    
	# Champs essentiels obligatoires (non nullable) mais avec des valeurs par défaut
    date_commande = Column(Date, nullable=False, default=func.now())
    timbre_commande = Column(Float, nullable=False, default=0.0)
    timbre_client = Column(Float, nullable=False, default=0.0)
    cheque_client = Column(Float, nullable=False, default=0.0)
    
    # Champs optionnels pouvant être NULL
    commentaire_commande = Column(String(255), nullable=True, default=None)
    
    __table_args__ = (
        Index('commande_index', "commentaire_commande", "client_id"),
        CheckConstraint(date_commande >= '2020-01-01', name='check_date_commande'),
        CheckConstraint(timbre_commande >= 0, name='check_timbre_commande'),
        CheckConstraint(timbre_client >= 0, name='check_timbre_client'),
        CheckConstraint(cheque_client >= 0, name='check_cheque_client')
    )

    def __repr__(self):
        return (
            f"<Commande(commande_id={self.commande_id}, date_commande='{self.date_commande}', "
            f"client_id={self.client_id}, timbre_commande={self.timbre_commande}, "
            f"timbre_client={self.timbre_client}, cheque_client={self.cheque_client}, "
            f"commentaire_commande='{self.commentaire_commande}')>"
        )
