from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Variables globales
created_id = None
cli_data = {
    "genre": "M",
    "nom": "Doe",
    "prenom": "John",
    "adresse_ligne1": "1 rue de la Paix",
    "tel": "0123456789",
    "email": "john.doe@gmail.com",
    "newsletter": 0
}
update_cli ={
    "genre": "F",
    "nom": "Doe",
    "prenom": "Jane",
    "adresse_ligne1": "1 rue de la Paix",
    "tel": "0123456789",
    "email": "jane.doe@gmail.com",
    "newsletter": 1
}


def test_get_all_clients():
    response = client.get("/client/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_client():
    global created_id  # Nous déclarons global car nous voulons modifier cette variable à l'échelle globale
    reponse = client.post("/client/", json=cli_data)
    
    # Comparer les données du client créées avec celles renvoyées par l'API
    data = reponse.json()
    created_id = data["client_id"]  # Assigner le client_id retourné
    assert reponse.status_code == 200
    assert data["genre"] == cli_data["genre"]
    assert data["nom"] == cli_data["nom"].upper()
    assert data["prenom"] == cli_data["prenom"].capitalize()
    assert data["adresse_ligne1"] == cli_data["adresse_ligne1"]
    assert data["tel"] == cli_data["tel"]
    assert data["email"] == cli_data["email"].lower()
    assert data["newsletter"] == cli_data["newsletter"]


def test_get_client_by_id():
    assert created_id is not None, "Le client n'a pas été créé avant d'essayer de le récupérer"
    
    response = client.get(f"/client/{created_id}")
    assert response.status_code == 200
    data = response.json()
    
    # Comparer les données du client créées avec celles renvoyées par l'API
    assert data["client_id"] == created_id
    assert data["genre"] == cli_data["genre"]
    assert data["nom"] == cli_data["nom"].upper()
    assert data["prenom"] == cli_data["prenom"].capitalize()
    assert data["adresse_ligne1"] == cli_data["adresse_ligne1"]
    assert data["tel"] == cli_data["tel"]
    assert data["email"] == cli_data["email"].lower()
    assert data["newsletter"] == cli_data["newsletter"]


def test_get_client_by_name():
    assert created_id is not None, "Le client n'a pas été créé avant d'essayer de le récupérer"
    
    response = client.get(f"/client/{cli_data['nom']}/{cli_data['prenom']}")
    assert response.status_code == 200
    data = response.json()
    
    # Comparer les données du client créées avec celles renvoyées par l'API
    assert data["client_id"] == created_id
    assert data["genre"] == cli_data["genre"]
    assert data["nom"] == cli_data["nom"].upper()
    assert data["prenom"] == cli_data["prenom"].capitalize()
    assert data["adresse_ligne1"] == cli_data["adresse_ligne1"]
    assert data["tel"] == cli_data["tel"]
    assert data["email"] == cli_data["email"].lower()
    assert data["newsletter"] == cli_data["newsletter"]
    
    
def test_get_client_by_email():
    assert created_id is not None, "Le client n'a pas été créé avant d'essayer de le récupérer"
    
    response = client.get(f"/client/email/{cli_data['email']}")
    assert response.status_code == 200
    data = response.json()
    
    # Comparer les données du client créées avec celles renvoyées par l'API
    assert data["client_id"] == created_id
    assert data["genre"] == cli_data["genre"]
    assert data["nom"] == cli_data["nom"].upper()
    assert data["prenom"] == cli_data["prenom"].capitalize()
    assert data["adresse_ligne1"] == cli_data["adresse_ligne1"]
    assert data["tel"] == cli_data["tel"]
    assert data["email"] == cli_data["email"].lower()
    assert data["newsletter"] == cli_data["newsletter"]


def test_patch_client():
    assert created_id is not None, "Le client n'a pas été créé avant d'essayer de le mettre à jour"
    
    response = client.patch(f"/client/{created_id}", json=update_cli)
    assert response.status_code == 200
    
    # Comparer les données du client mises à jour avec celles renvoyées par l'API
    data = response.json()
    assert data["client_id"] == created_id
    assert data["genre"] == update_cli["genre"]
    assert data["nom"] == update_cli["nom"].upper()
    assert data["prenom"] == update_cli["prenom"].capitalize()
    assert data["adresse_ligne1"] == update_cli["adresse_ligne1"]
    assert data["tel"] == update_cli["tel"]
    assert data["email"] == update_cli["email"].lower()
    assert data["newsletter"] == update_cli["newsletter"]


def test_delete_client():
    assert created_id is not None, "Le client n'a pas été créé avant d'essayer de le supprimer"
    
    response = client.delete(f"/client/{created_id}")
    assert response.status_code == 200
    data = response.json()
    
    # Vérifier que le client supprimé est le bon
    assert data["client_id"] == created_id
