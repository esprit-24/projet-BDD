from flask import Blueprint, request, jsonify
import requests
from config import UGB_URL, UAD_URL, TIMEOUT

routes = Blueprint("routes", __name__)

# ==========================
# Helpers HTTP sécurisés
# ==========================
def safe_get(url):
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return None

def safe_post(url, payload):
    try:
        r = requests.post(url, json=payload, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json(), r.status_code
    except Exception as e:
        return {"erreur": str(e)}, 500

# ==========================
# 1️⃣ Tous les étudiants (fusion)
# ==========================
@routes.route("/etudiants", methods=["GET"])
def tous_les_etudiants():
    etu_ugb = safe_get(f"{UGB_URL}/etudiants") or []
    etu_uad = safe_get(f"{UAD_URL}/etudiants") or []

    # Marquer l’origine
    for e in etu_ugb:
        e["universite_origine"] = "UGB"
    for e in etu_uad:
        e["universite_origine"] = "UAD"

    return jsonify(etu_ugb + etu_uad)

# ==========================
# 2️⃣ Étudiants ayant fait des emprunts (global)
# ==========================
@routes.route("/etudiants/emprunteurs", methods=["GET"])
def etudiants_emprunteurs():
    emp_ugb = safe_get(f"{UGB_URL}/etudiants/emprunteurs") or []
    emp_uad = safe_get(f"{UAD_URL}/etudiants/emprunteurs") or []

    for e in emp_ugb:
        e["universite_origine"] = "UGB"
    for e in emp_uad:
        e["universite_origine"] = "UAD"

    return jsonify(emp_ugb + emp_uad)

# ==========================
# 3️⃣ Tous les ouvrages (fusion)
# ==========================
@routes.route("/ouvrages", methods=["GET"])
def tous_les_ouvrages():
    ouv_ugb = safe_get(f"{UGB_URL}/ouvrages") or []
    ouv_uad = safe_get(f"{UAD_URL}/ouvrages") or []

    for o in ouv_ugb:
        o["site"] = "UGB"
    for o in ouv_uad:
        o["site"] = "UAD"

    return jsonify(ouv_ugb + ouv_uad)

# ==========================
# 4️⃣ Créer un emprunt distribué (logique centrale)
# ==========================
@routes.route("/emprunt", methods=["POST"])
def creer_emprunt():
    data = request.json
    if not data:
        return jsonify({"erreur": "Données manquantes"}), 400

    universite = data.get("universite")  # université de l'étudiant
    idEtud = data.get("idEtud")
    idOuv = data.get("idOuv")
    date_emprunt = data.get("date_emprunt")
    date_retour = data.get("date_retour")

    if not all([universite, idEtud, idOuv, date_emprunt]):
        return jsonify({"erreur": "Champs requis manquants"}), 400

    # Choix du service selon l’université d’origine de l’étudiant
    if universite == "UGB":
        service = UGB_URL
    elif universite == "UAD":
        service = UAD_URL
    else:
        return jsonify({"erreur": "Université invalide (UGB ou UAD)"}), 400

    # Vérifier existence étudiant
    etu = safe_get(f"{service}/etudiants/{idEtud}")
    if not etu:
        return jsonify({"erreur": "Étudiant introuvable"}), 404

    # Vérifier existence ouvrage (dans toutes les bibliothèques)
    ouvrages = safe_get(f"{UGB_URL}/ouvrages") or []
    ouvrages += safe_get(f"{UAD_URL}/ouvrages") or []

    ouvrage = next((o for o in ouvrages if o["idOuv"] == idOuv), None)
    if not ouvrage:
        return jsonify({"erreur": "Ouvrage introuvable"}), 404

    if ouvrage["stock"] <= 0:
        return jsonify({"erreur": "Ouvrage indisponible"}), 409

    # Créer le prêt dans l’université d’origine de l’étudiant
    payload = {
        "idEtud": idEtud,
        "idOuv": idOuv,
        "date_emprunt": date_emprunt,
        "date_retour": date_retour
    }

    response, status = safe_post(f"{service}/prets", payload)
    return jsonify(response), status

# ==========================
# Accueil / documentation
# ==========================
@routes.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Microservice Bibliothèque Universitaire",
        "role": "Distribution et agrégation des données",
        "endpoints": {
            "GET /etudiants": "Tous les étudiants (UGB + UAD)",
            "GET /etudiants/emprunteurs": "Étudiants ayant emprunté",
            "GET /ouvrages": "Tous les ouvrages",
            "POST /emprunt": "Créer un emprunt distribué"
        }
    })
