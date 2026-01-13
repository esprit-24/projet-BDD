# 📚 Projet Bases de Données Distribuées  
## Bibliothèque Universitaire Distribuée (UGB / UAD)

Ce projet met en œuvre une **architecture distribuée** pour la gestion d’une bibliothèque universitaire, conformément au sujet du module *Bases de Données Distribuées*.

Le système repose sur :
- Deux bases de données hétérogènes :
  - **UGB** → MySQL
  - **UAD** → PostgreSQL
- Deux services locaux (UGB et UAD)
- Un **microservice central** d’orchestration
- Une **interface web intégrée** permettant de tester l’ensemble des fonctionnalités

---

## 🧱 Architecture du projet

```
projet-BDD/
│
├── docker-compose.yml
│
├── docker/
│   ├── mysql/
│   │   └── init/
│   │       └── site_ugb.sql
│   └── postgres/
│       └── init/
│           └── site_uad.sql
│
├── ugb_service/
│   ├── app.py
│   ├── routes.py
│   └── db.py
│
├── uad_service/
│   ├── app.py
│   ├── routes.py
│   └── db.py
│
├── microservice/
│   ├── microservice.py
│   ├── routes.py
│   └── config.py
│
└── templates/
    └── index.html
```

---

## ⚙️ Prérequis

- Git  
- Docker & Docker Compose  
- Python 3.9+  
- pip  

---

## 🧭 Cloner et lancer le projet

```bash
git clone https://github.com/esprit-24/projet-BDD.git
cd projet-BDD
git branch -a
git checkout esprit
```

---

## 🐳 Lancer les bases de données

```bash
docker-compose up -d
```

Ports :
- MySQL (UGB) : 3307  
- PostgreSQL (UAD) : 5433  

---

## 🐍 Installer les dépendances

```bash
pip install flask flask-cors pymysql psycopg2-binary requests
```

---

## ▶️ Lancer les services (ordre important)

### Service UGB
```bash
cd ugb_service
python app_ugb.py
```

### Service UAD
```bash
cd uad_service
python app_uad.py
```

### Microservice
```bash
cd microservice
python microservice.py
```

---

## 🌐 Interface Web

Ouvrir simplement :
```
templates/index.html
```

---

## 🔐 Règles métier

- Limite du nombre d’emprunts par étudiant  
- Vérification du stock  
- Mise à jour automatique du stock et des emprunts  
- Clé composée (idOuv, site) pour les ouvrages  

---

## ✅ État du projet

✔️ Fonctionnel  
✔️ Conforme au sujet  
✔️ Prêt pour soutenance  
