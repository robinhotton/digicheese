import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import app
import unittest
from fastapi.testclient import TestClient
from typing import List

class TestHomeRoute(unittest.TestCase):
    def setUp(self):
        self.created_id = None
        self.client = TestClient(app)
        
    def test_route_hello_world(self):
        reponse = self.client.get("/")
        self.assertEqual(reponse.status_code, 200) # reussite
        self.assertEqual(reponse.json(), {"message": "Bienvenue sur notre API DIGICHEESE"}) # bon le json
        
        
    def test_create_client(self):
        new_cli = {
            "genrecli": "Monsieur",
            "nomcli": "Doe",
            "prenomcli": "John",
            "adresse1cli": "1 rue de la Paix",
            "telcli": "0123456789",
            "emailcli": "john.doe@gmail.com",
            "newsletter": 0
        }
        reponse = self.client.post("/clients/", json=new_cli)
        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(reponse.json()["genrecli"], "Monsieur")
        self.assertEqual(reponse.json()["nomcli"], "Doe")
        self.assertEqual(reponse.json()["prenomcli"], "John")
        self.assertEqual(reponse.json()["adresse1cli"], "1 rue de la Paix")
        self.assertEqual(reponse.json()["telcli"], "0123456789")
        self.assertEqual(reponse.json()["emailcli"], "john.doe@gmail.com")
        self.assertEqual(reponse.json()["newsletter"], 0)
        
        
    def test_read_clients(self):
        reponse = self.client.get("/clients/")
        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(type(reponse.json()), List)
        
        # renverser la liste pour avoir l'id du dernier client inséré
        self.created_id = reponse.json()[::-1][0]["codcli"]
        
    def test_read_client(self):
        reponse = self.client.get(f"/clients/{self.created_id}")
        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(reponse.json()["codcli"], self.created_id)
        
        
    def test_update_client(self):
        update_cli = {
            "genrecli": "Madame",
            "nomcli": "Doe",
            "prenomcli": "Jane",
            "adresse1cli": "1 rue de la Paix",
            "telcli": "0123456789",
            "emailcli": "jane.doe@gmail.com",
            "newsletter": 1
        }
        reponse = self.client.put(f"/clients/{self.created_id}", json=update_cli)
        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(reponse.json()["genrecli"], "Madame")
        self.assertEqual(reponse.json()["nomcli"], "Doe")
        self.assertEqual(reponse.json()["prenomcli"], "Jane")
        self.assertEqual(reponse.json()["adresse1cli"], "1 rue de la Paix")
        self.assertEqual(reponse.json()["telcli"], "0123456789")
        self.assertEqual(reponse.json()["emailcli"], "jane.doe@gmail.com")
        self.assertEqual(reponse.json()["newsletter"], 1)
        
        
    def test_delete_client(self):
        reponse = self.client.delete(f"/clients/{self.created_id}")
        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(reponse.json()["codcli"], self.created_id)
        

if __name__ == "__main__":
    unittest.main()