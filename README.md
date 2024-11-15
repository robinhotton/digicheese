# Projet FastAPI - Digicheese

Ce projet est une API RESTful construite avec **FastAPI** qui permet de gérer des informations sur des clients (création, récupération, mise à jour, suppression). L'API expose des endpoints pour interagir avec des données de clients, y compris les informations de contact, le genre, le statut de la newsletter, et plus encore.

## Sommaire

- [Description du Projet](#description-du-projet)
- [Dépendances](#dépendances)
- [Endpoints](#endpoints)
- [Architecture du Projet](#architecture-du-projet)
- [Installation et Lancement](#installation-et-lancement)
- [Tests](#tests)

---

## Description du Projet

Ce projet consiste en une API permettant de gérer des **clients**. Un client est défini par un certain nombre d'attributs tels que le genre, le nom, le prénom, l'adresse, le téléphone, l'email et l'abonnement à une newsletter. L'API offre les fonctionnalités suivantes :

- **Création** d'un client
- **Lecture** de tous les clients ou d'un client spécifique par ID, nom, prénom ou email
- **Mise à jour** des informations d'un client
- **Suppression** d'un client

Cette API est construite avec **FastAPI**, qui est un framework moderne et rapide pour construire des APIs avec Python 3.7+.

---

## Dépendances

Les dépendances principales pour ce projet sont les suivantes :

- **FastAPI** : le framework pour construire l'API.
- **Uvicorn** : le serveur ASGI pour exécuter l'application.
- **Pydantic** : pour la validation des données et la gestion des schémas.
- **SQLAlchemy** : pour la gestion de la base de données.
- **fastapi.testclient** : pour tester l'API via une simulation de requêtes HTTP.
- **pytest** : pour les tests unitaires.

### Installation des dépendances

Avant de commencer, assurez-vous d'avoir **Python 3.7+** installé.

1. Clonez ce dépôt sur votre machine locale :

    ```bash
    git clone https://github.com/robinhotton/digicheese.git
    cd digicheese
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Linux/macOS
    venv\Scripts\activate     # Sur Windows
    ```

3. Installez les dépendances nécessaires :

    ```bash
    pip install -r requirements.txt
    ```

---

## Endpoints

L'API expose les endpoints suivants :

### 1. **GET /client/**

Récupère la liste de tous les clients.

**Réponse :**

```json
[
    {
        "client_id": 1,
        "genre": "M",
        "nom": "Doe",
        "prenom": "John",
        "adresse_ligne1": "1 rue de la Paix",
        "tel": "0123456789",
        "email": "john.doe@gmail.com",
        "newsletter": 0
    },
    ...
]
```

### 2. **POST /client/**

Crée un nouveau client. Attends un corps de requête contenant les informations du client.

**Corps de la requête :**

```json
{
    "genre": "M",
    "nom": "Doe",
    "prenom": "John",
    "adresse_ligne1": "1 rue de la Paix",
    "tel": "0123456789",
    "email": "john.doe@gmail.com",
    "newsletter": 0
}
```

**Réponse :**

```json
{
    "client_id": 1,
    "genre": "M",
    "nom": "Doe",
    "prenom": "John",
    "adresse_ligne1": "1 rue de la Paix",
    "tel": "0123456789",
    "email": "john.doe@gmail.com",
    "newsletter": 0
}
```

### 3. **GET /client/{client_id}**

Récupère un client spécifique par son `client_id`.

**Réponse :**

```json
{
    "client_id": 1,
    "genre": "M",
    "nom": "Doe",
    "prenom": "John",
    "adresse_ligne1": "1 rue de la Paix",
    "tel": "0123456789",
    "email": "john.doe@gmail.com",
    "newsletter": 0
}
```

### 4. **GET /client/{nom}/{prenom}**

Récupère un client par son nom et prénom.

**Réponse :**

```json
{
    "client_id": 1,
    "genre": "M",
    "nom": "Doe",
    "prenom": "John",
    "adresse_ligne1": "1 rue de la Paix",
    "tel": "0123456789",
    "email": "john.doe@gmail.com",
    "newsletter": 0
}
```

### 5. **GET /client/email/{email}**

Récupère un client par son email.

**Réponse :**

```json
{
    "client_id": 1,
    "genre": "M",
    "nom": "Doe",
    "prenom": "John",
    "adresse_ligne1": "1 rue de la Paix",
    "tel": "0123456789",
    "email": "john.doe@gmail.com",
    "newsletter": 0
}
```

### 6. **PATCH /client/{client_id}**

Met à jour les informations d'un client spécifique.

**Corps de la requête :**

```json
{
    "genre": "F",
    "nom": "Doe",
    "prenom": "Jane",
    "adresse_ligne1": "1 rue de la Paix",
    "tel": "0123456789",
    "email": "jane.doe@gmail.com",
    "newsletter": 1
}
```

**Réponse :**

```json
{
    "client_id": 1,
    "genre": "F",
    "nom": "Doe",
    "prenom": "Jane",
    "adresse_ligne1": "1 rue de la Paix",
    "tel": "0123456789",
    "email": "jane.doe@gmail.com",
    "newsletter": 1
}
```

### 7. **DELETE /client/{client_id}**

Supprime un client spécifique.

**Réponse :**

```json
{
    "client_id": 1,
    "genre": "F",
    "nom": "Doe",
    "prenom": "Jane",
    "adresse_ligne1": "1 rue de la Paix",
    "tel": "0123456789",
    "email": "jane.doe@gmail.com",
    "newsletter": 1
}
```

---

## Architecture du Projet

```bash
digicheese/
│
├── src/
│   ├── models/               # Modèles de données SQLAlchemy
│   ├── schemas/              # Schémas de validation de données (Pydantic)
│   ├── repositories/         # Gestion des accès à la base de données
│   ├── services/             # Logique métier
│   ├── routers/              # Définition des routes de l'API
│   ├── database.py           # Configuration de la base de données et connexion
│   └── main.py               # Application principale (point d'entrée FastAPI)
│
├── tests/                    # Tests unitaires
│
├── .gitignore                # Fichier pour ignorer certains fichiers/dossiers dans git
├── .env                      # Fichier pour les variables d'environnement
├── .env.example              # Exemple de fichier .env
├── .venv/                    # Dossier pour l'environnement virtuel Python
├── requirements.txt          # Liste des dépendances du projet
├── README.md                 # Documentation du projet
└── run.py                    # Fichier principal pour démarrer l'application
```

---

## Installation et Lancement

### Lancer l'API

1. Assurez-vous que les dépendances sont installées (voir la section **Installation des dépendances**).
2. Pour démarrer le serveur de l'API, utilisez la commande suivante :

   ```bash
   python run.py # ou uvicorn src.main:app --reload
   ```

   Cela démarrera l'API en mode développement avec rechargement automatique (`--reload`).

### Accéder à l'API

L'API sera disponible à l'adresse suivante :

```bash
http://127.0.0.1:8000
```

Vous pouvez aussi accéder à la documentation interactive de l'API à l'adresse suivante :

```bash
http://127.0.0.1:8000/docs
```

---

## Tests

1. Si vous utilisez **pytest**, vous pouvez lancer tous les tests en exécutant la commande suivante :

   ```bash
   pytest
   ```

   Cela exécutera tous les tests définis dans le répertoire `tests/`.

---

## Auteur

- **Robin Hotton** - [robinhotton](https://github.com/robinhotton)
