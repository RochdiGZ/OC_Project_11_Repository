## Projet 11 : Améliorez une application web Python par des tests et du débogage
### 📖 Vue d'ensemble
Améliorer une Plateforme de réservation de places à des compétitions de force (deadlifting, strongman) pour la société
Güdlft en Amérique du Nord et en Australie.
L'objectif du projet est de corriger les erreurs et bogues, présents dans le dépôt du GitHub ayant le lien suivant :
`https://github.com/OpenClassrooms-Student-Center/Python_Testing`, et d'ajouter de nouvelles fonctionnalités.
Chaque correction/ajout se trouve sur sa propre branche en utilisant :

💿 Windows 10 💿 Python 3.11.3 💿 PyCharm 2023.1.1 💿 Flake8 4.0.1 💿 Flake8-html 0.4.2 💿 Git 2.40.1 💿 Flask 2.3.2 💿

💿 Coverage 7.2.5 💿 Pytest 7.3.1 💿 Locust 2.15.1 💿

### 📖 Clonage du projet depuis GitHub
```bash
git clone https://github.com/RochdiGZ/OC_Project_11_Repository.git
```

## 📖 Modification des propriétés du dossier OC_Project_11_Repository comme source de données
-  À l'aide de PyCharm, il suffit de sélectionner le dossier et d'utiliser le bouton droit de la souris pour choisir 
`Mark Directory as > Sources Root`

### 📖 Création et activation d'un nouvel environnement virtuel `env`
```bash
cd OC_Project_11_Repository
```
```bash
python -m venv env
```
```bash
env/Scripts/activate
```

### 📖 Choix de l'interpréteur Python

### 📖 Installation de toutes les dépendances nécessaires à l'exécution de l'application
```bash
python.exe -m pip install --upgrade pip
``` 
```bash
pip install -r requirements.txt
```

### 📖 Lancement du serveur de développement Flask
```bash
$env:FLASK_APP = "server.py"
```
```bash
flask run
```

### 📖 Accès à la page d'accueil du site web via `http://127.0.0.1:5000/`

### 📖 Affichage du nombre de points disponibles pour chaque club via `http://127.0.0.1:5000/clubs-points`

### 📖 Connexion à l'aide de l'email du club via `http://127.0.0.1:5000/`
Tous les emails se figurent dans le fichier `clubs.json`

### 📖 Affichage des informations de toutes les compétitions via `http://127.0.0.1:5000/show_summary` 

### 📖 Réservation des places à une compétition ouverte via 
### `http://127.0.0.1:5000/book/<competition_name>/<club_name>`

### 📖 Confirmation de la réservation via `http://127.0.0.1:5000/purchase_places` 

### 📖 Tests
Toutes les dépendances nécessaires à l'exécution des tests sont inclus dans `requirements.txt`.
`Les tests unitaires et d'intégration sont exécutés grâce à Pytest (version 7.3.1).`
Pour effectuer l'ensemble des tests unitaires et d'intégration, il suffit de taper la commande :
```bash
pytest
```
`Le module Coverage (version 7.2.5) est installé pour obtenir le rapport de couverture des tests via les 2 commandes :`
```bash
coverage run -m pytest
```
```bash
coverage html
```
Pour effectuer l'ensemble des `tests de performance` grâce au module Locust (version 2.15.1), il suffit de taper 
les commandes suivantes :
```bash
cd tests
```
```bash
cd performance_tests
```
```bash
locust -f locustfile.py
```
-- Dans le cas où le fichier est nommé `locustfile.py` :
On pourra taper `locust` au lieu de `locust -f locustfile.py`
### 📖 Lancement du serveur de développement Locust via http://localhost:8089
- Taper le nombre d'utilisateurs (par exemple : `6`)
- Taper le nombre d'utilisateurs démarrés par seconde (par exemple : `1`)
- Taper l'adresse de l'hôte (host), l'adresse de notre application, `http://127.0.0.1:5000/`
- Cliquer sur le bouton `Start Swarming`

-- Dans le cas où le fichier est nommé `locustfile2.py` : 
- On tape la commande :
```bash
locust -f locustfile2.py
```
- On lance de nouveau le serveur de développement Locust via http://localhost:8089

### 📖 Rapports de tests
Les captures d'écran des derniers rapports de tests sont disponibles dans les livrables du projet :

`Rapport de couverture des tests` (GUEZGUEZ_Rochdi_02_Rapport_Test_Coverage_042023.png)

`Rapport de tests de performance` (GUEZGUEZ_Rochdi_02_Rapport_Test_Locust_042023.png)

### 📖 Information utile
Pour toute information sur les besoins d'exécution de l'application GÜDLFT, veuillez me contacter par email :
`Rochdi.GUEZGUEZ@Gmail.Com`
