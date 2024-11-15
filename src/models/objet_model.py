from sqlalchemy import Column, Float, Integer, String, CheckConstraint
from src.models.base_model import Base

class Objet(Base):
    __tablename__ = "t_objet"

	# Champs obligatoires
    objet_id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)
    
    # nullable ou obligatoire avec une valeur par défaut
    taille = Column(String(50), nullable=True, default=None)
    prix_unitaire = Column(Float, nullable=False, default=0.0)
    poids = Column(Float, nullable=False, default=0.0)
    points = Column(Integer, nullable=False, default=0)

    # Contrainte sur le prix, poids et points : ces valeurs ne doivent pas être négatives
    __table_args__ = (
        CheckConstraint('prix_unitaire >= 0', name='check_prix_unitaire'),
        CheckConstraint('poids >= 0', name='check_poids'),
        CheckConstraint('points >= 0', name='check_points'),
    )

    def __repr__(self):
        return (
            f"<Objet(objet_id={self.objet_id}, libelle='{self.libelle}', taille='{self.taille}', "
            f"prix_unitaire={self.prix_unitaire}, poids={self.poids}, points={self.points})>"
        )
