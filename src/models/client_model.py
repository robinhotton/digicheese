from src.models.base_model import Base
from sqlalchemy import CheckConstraint, Column, Integer, String, Boolean


class Client(Base):
    __tablename__ = "t_client"

    # Champs obligatoires
    client_id = Column(Integer, primary_key=True)
    nom = Column(String(40), nullable=False, index=True)  # Nom obligatoire
    prenom = Column(String(30), nullable=False)  # Prénom obligatoire
    
    # Champs optionnels pouvant être NULL
    genre = Column(String(8), nullable=True, default=None)
    adresse_ligne1 = Column(String(50), nullable=True, default=None)
    adresse_ligne2 = Column(String(50), nullable=True, default=None)
    adresse_complement = Column(String(50), nullable=True, default=None)
    tel = Column(String(10), nullable=True, default=None)
    email = Column(String(50), nullable=True, default=None)
    
    # Champ de la newsletter Obligatoire mais avec une valeur par défaut
    newsletter = Column(Boolean, default=False, nullable=False)
    
    __table_args__ = (
        CheckConstraint(email.like('%@%.%'), name='check_email'),
        CheckConstraint(tel.like('%[0-9]%'), name='check_tel'),
        CheckConstraint(genre.in_(['M', 'F', 'Autre']), name='check_genre'),
        CheckConstraint(newsletter.in_([0, 1]), name='check_newsletter')
    )
        
    def __repr__(self):
        return (
            f"<Client(client_id={self.client_id}, nom='{self.nom}', prenom='{self.prenom}', "
            f"genre='{self.genre}', adresse_ligne1='{self.adresse_ligne1}', adresse_ligne2='{self.adresse_ligne2}', "
            f"adresse_complement='{self.adresse_complement}', tel='{self.tel}', "
            f"email='{self.email}', newsletter={self.newsletter})>"
        )
