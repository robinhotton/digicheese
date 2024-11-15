from src.models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint


class Detail(Base):
    __tablename__ = "t_detail_commande"

	# colonnes de la table
    detail_id = Column(Integer, primary_key=True)
    commande_id = Column(Integer, ForeignKey('t_commande.commande_id', ondelete='CASCADE'), nullable=False, index=True)
    quantite = Column(Integer, nullable=False, default=1)
    commentaire = Column(String(100), nullable=True, default=None)

    # Contrainte pour garantir que la quantité est positive
    __table_args__ = (
        CheckConstraint('quantite >= 1', name='quantite_positive'),
    )

    def __repr__(self):
        return (
            f"<Detail(detail_id={self.detail_id}, commande_id={self.commande_id}, "
            f"quantite={self.quantite}, commentaire='{self.commentaire}')>"
        )
