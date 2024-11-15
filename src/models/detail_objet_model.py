from sqlalchemy import Column, Index, Integer, ForeignKey, PrimaryKeyConstraint
from .base_model import Base

class DetailObjet(Base):
    __tablename__ = "t_detail_commande_objet"

    # Les colonnes pour les clés étrangères
    detail_id = Column(Integer, ForeignKey('t_detail_commande.detail_id', ondelete='CASCADE'), nullable=False)
    objet_id = Column(Integer, ForeignKey('t_objet.objet_id', ondelete='CASCADE'), nullable=False)

    # Contrainte de clé primaire composite
    __table_args__ = (
        PrimaryKeyConstraint('detail_id', 'objet_id', name='pk_detail_objet'),
        Index('idx_detail_objet', 'detail_id', 'objet_id')  # Index sur les deux colonnes
    )

    def __repr__(self):
        return (
            f"<DetailObjet(detail_id={self.detail_id}, objet_id={self.objet_id})>"
        )
