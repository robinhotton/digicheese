import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import app
import unittest
from fastapi.testclient import TestClient
from typing import List

class TestHomeRoute(unittest.TestCase):
    created_id = None
    
    def setUp(self):
        self.client = TestClient(app)
        
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
        data = reponse.json()
        print(data)
        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(data["genrecli"], "Monsieur")
        self.assertEqual(data["nomcli"], "Doe")
        self.assertEqual(data["prenomcli"], "John")
        self.assertEqual(data["adresse1cli"], "1 rue de la Paix")
        self.assertEqual(data["telcli"], "0123456789")
        self.assertEqual(data["emailcli"], "john.doe@gmail.com")
        self.assertEqual(data["newsletter"], 0)
        
        
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
        reponse = self.client.patch(f"/clients/{self.created_id}", json=update_cli)
        self.assertEqual(reponse.status_code, 200)
        data = reponse.json()
        self.assertEqual(data["genrecli"], "Madame")
        self.assertEqual(data["nomcli"], "Doe")
        self.assertEqual(data["prenomcli"], "Jane")
        self.assertEqual(data["adresse1cli"], "1 rue de la Paix")
        self.assertEqual(data["telcli"], "0123456789")
        self.assertEqual(data["emailcli"], "jane.doe@gmail.com")
        self.assertEqual(data["newsletter"], 1)
        
        
    def test_delete_client(self):
        reponse = self.client.delete(f"/clients/{self.created_id}")
        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(reponse.json()["codcli"], self.created_id)
        

if __name__ == "__main__":
    unittest.main()