from sqlalchemy.orm import Session
from ..repository import ClientRepository
from ..schemas import ClientCreate, ClientUpdate


class ClientService:
    repository = ClientRepository()


    def fetch_all_clients(self, db: Session):
        return self.repository.get_all_clients(db)


    def fetch_client_by_id(self, db: Session, client_id: int):
        client = self.repository.get_client_by_id(db, client_id)
        if not client:
            raise ValueError("Client not found")
        return client
    
    
    def fetch_client_by_email(self, db: Session, email: str):
        formatted_email = email.lower()
        client = self.repository.get_client_by_email(db, formatted_email)
        if not client:
            raise ValueError("Client not found")
        return client
    
    
    def fetch_client_by_name(self, db: Session, nom: str, prenom: str):
        client = self.repository.get_client_by_name(db, nom, prenom)
        if not client:
            raise ValueError("Client not found")
        return client


    def add_client(self, db: Session, client_data: ClientCreate):
        data = self.__transform_client_data(client_data.model_dump())
        return self.repository.create_client(db, data)


    def patch_client(self, db: Session, client_id: int, client_data: ClientUpdate):
        data = self.__transform_client_data(client_data.model_dump(exclude_unset=True))
        updated_client = self.repository.update_client(db, client_id, data)
        if not updated_client:
            raise ValueError("Client not found for update")
        return updated_client


    def remove_client(self, db: Session, client_id: int):
        client = self.repository.delete_client(db, client_id)
        if not client:
            raise ValueError("Client not found for deletion")
        return client
    
    
    def __transform_client_data(self, data: dict) -> dict:
        """
        Transforme les données du client (par exemple, capitalisation des noms, transformation en minuscules des emails).
        
        Args:
        - data (dict): Le dictionnaire contenant les données du client.

        Returns:
        - dict: Le dictionnaire transformé avec les valeurs adaptées.
        """
        for key, value in data.items():
            if value is None:
                continue  # Skip None values, no transformation needed

            if isinstance(value, str):  # For string fields
                if key == "nom":
                    data[key] = value.upper()  # Transform "nom" to uppercase
                elif key == "prenom":
                    data[key] = value.capitalize()  # Capitalize the "prenom"
                elif key == "email":
                    data[key] = value.lower()  # Make "email" lowercase
                else:
                    data[key] = value.strip()  # Optionally strip whitespace for other strings
            elif isinstance(value, bool):  # If the value is a boolean
                if isinstance(value, int):  # Convert integer (0 or 1) to bool
                    data[key] = bool(value)
        
        return data
