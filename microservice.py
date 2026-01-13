from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# ==========================
# Configuration
# ==========================
UGB = "http://127.0.0.1:5001"
UAD = "http://127.0.0.1:5002"
TIMEOUT = 5

# ==========================
# Helpers HTTP sécurisés
# ==========================
def safe_get(url):
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {
            "status": "indisponible",
            "service": url,
            "erreur": str(e)
        }

def safe_post(url, payload):
    try:
        r = requests.post(url, json=payload, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json(), r.status_code
    except Exception as e:
        return {
            "status": "echec",
            "service": url,
            "erreur": str(e)
        }, 500

# ==========================
# 1️⃣ Tous les étudiants
# ==========================
@app.route("/etudiants", methods=["GET"])
def tous_les_etudiants():
    return jsonify({
        "UGB": safe_get(f"{UGB}/etudiants"),
        "UAD": safe_get(f"{UAD}/etudiants")
    })

# ==========================
# 2️⃣ Tous les ouvrages
# ==========================
@app.route("/ouvrages", methods=["GET"])
def tous_les_ouvrages():
    return jsonify({
        "UGB": safe_get(f"{UGB}/ouvrages"),
        "UAD": safe_get(f"{UAD}/ouvrages")
    })

# ==========================
# 3️⃣ Tous les emprunts
# ==========================
@app.route("/emprunts", methods=["GET"])
def tous_les_emprunts():
    return jsonify({
        "UGB": safe_get(f"{UGB}/prets"),
        "UAD": safe_get(f"{UAD}/prets")
    })

# ==========================
# 4️⃣ Créer un emprunt distribué
# ==========================
@app.route("/emprunt", methods=["POST"])
def faire_emprunt():
    data = request.json

    if not data:
        return jsonify({"erreur": "Données manquantes"}), 400

    universite = data.get("universite")
    idetud = data.get("idetud")
    idouv = data.get("idouv")
    date_emprunt = data.get("date_emprunt")
    date_retour = data.get("date_retour")

    if not all([universite, idetud, idouv, date_emprunt]):
        return jsonify({"erreur": "Champs requis manquants"}), 400

    payload = {
        "idEtud": idetud,
        "idOuv": idouv,
        "date_emprunt": date_emprunt,
        "date_retour": date_retour
    }

    if universite == "UGB":
        response, status = safe_post(f"{UGB}/prets", payload)
    elif universite == "UAD":
        response, status = safe_post(f"{UAD}/prets", payload)
    else:
        return jsonify({"erreur": "Université invalide (UGB ou UAD)"}), 400

    return jsonify(response), status

# ==========================
# 5️⃣ Statistiques globales
# ==========================
@app.route("/statistiques", methods=["GET"])
def statistiques():
    etudiants_ugb = safe_get(f"{UGB}/etudiants")
    etudiants_uad = safe_get(f"{UAD}/etudiants")
    ouvrages_ugb = safe_get(f"{UGB}/ouvrages")
    ouvrages_uad = safe_get(f"{UAD}/ouvrages")
    emprunts_ugb = safe_get(f"{UGB}/prets")
    emprunts_uad = safe_get(f"{UAD}/prets")

    def count(data):
        return len(data) if isinstance(data, list) else 0

    return jsonify({
        "UGB": {
            "etudiants": count(etudiants_ugb),
            "ouvrages": count(ouvrages_ugb),
            "emprunts": count(emprunts_ugb)
        },
        "UAD": {
            "etudiants": count(etudiants_uad),
            "ouvrages": count(ouvrages_uad),
            "emprunts": count(emprunts_uad)
        },
        "total": {
            "etudiants": count(etudiants_ugb) + count(etudiants_uad),
            "ouvrages": count(ouvrages_ugb) + count(ouvrages_uad),
            "emprunts": count(emprunts_ugb) + count(emprunts_uad)
        }
    })

# ==========================
# Accueil / documentation
# ==========================
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Micro-service Bibliothèque Universitaire",
        "architecture": "Bases de données distribuées (UGB MySQL + UAD PostgreSQL)",
        "role": "Orchestration et agrégation des données",
        "endpoints": {
            "GET /etudiants": "Tous les étudiants",
            "GET /ouvrages": "Tous les ouvrages",
            "GET /emprunts": "Tous les emprunts",
            "POST /emprunt": "Créer un emprunt distribué",
            "GET /statistiques": "Statistiques globales"
        }
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
