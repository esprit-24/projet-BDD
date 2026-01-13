from flask import Blueprint, request, jsonify
import requests
from config import UGB_URL, UAD_URL, TIMEOUT

routes = Blueprint("routes", __name__)

MAX_EMPRUNTS = 3  # règle métier globale

# ==========================
# Helpers HTTP sécurisés
# ==========================
def safe_get(url):
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()
    except Exception:
        return None

def safe_post(url, payload):
    try:
        r = requests.post(url, json=payload, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json(), r.status_code
    except Exception as e:
        return {"erreur": str(e)}, 500

# ==========================
# Étudiants (fusion)
# ==========================
@routes.route("/etudiants", methods=["GET"])
def tous_les_etudiants():
    etu_ugb = safe_get(f"{UGB_URL}/etudiants") or []
    etu_uad = safe_get(f"{UAD_URL}/etudiants") or []

    for e in etu_ugb:
        e["universite_origine"] = "UGB"
    for e in etu_uad:
        e["universite_origine"] = "UAD"

    return jsonify(etu_ugb + etu_uad)

# ==========================
# Étudiants emprunteurs
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
# Ouvrages (fusion)
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
# Emprunt distribué (clé composée)
# ==========================
@routes.route("/emprunt", methods=["POST"])
def creer_emprunt():
    data = request.json
    if not data:
        return jsonify({"erreur": "Données manquantes"}), 400

    universite = data.get("universite")
    site_ouvrage = data.get("siteOuvrage")
    idEtud = int(data.get("idEtud"))
    idOuv = int(data.get("idOuv"))
    date_emprunt = data.get("date_emprunt")

    if not all([universite, site_ouvrage, idEtud, idOuv, date_emprunt]):
        return jsonify({"erreur": "Champs requis manquants"}), 400

    # Choix du service étudiant
    if universite == "UGB":
        service = UGB_URL
    elif universite == "UAD":
        service = UAD_URL
    else:
        return jsonify({"erreur": "Université invalide"}), 400

    # Vérifier étudiant
    etu = safe_get(f"{service}/etudiants/{idEtud}")
    if not etu:
        return jsonify({"erreur": "Étudiant introuvable"}), 404

    # Règle métier : quota
    if etu["nbreEmprunts"] >= MAX_EMPRUNTS:
        return jsonify({
            "erreur": "Limite d’emprunts atteinte",
            "max": MAX_EMPRUNTS
        }), 403

    # Vérifier ouvrage par (idOuv, site)
    ouvrages = (safe_get(f"{UGB_URL}/ouvrages") or []) + \
               (safe_get(f"{UAD_URL}/ouvrages") or [])

    ouvrage = next(
        (o for o in ouvrages
         if o["idOuv"] == idOuv and o["site"] == site_ouvrage),
        None
    )

    if not ouvrage:
        return jsonify({"erreur": "Ouvrage introuvable"}), 404

    if ouvrage["stock"] <= 0:
        return jsonify({"erreur": "Ouvrage indisponible"}), 409

    # Création du prêt
    payload = {
        "idEtud": idEtud,
        "idOuv": idOuv,
        "date_emprunt": date_emprunt
    }

    response, status = safe_post(f"{service}/prets", payload)
    return jsonify(response), status

# ==========================
# Accueil
# ==========================
@routes.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Microservice Bibliothèque Universitaire",
        "regle_cle": "Identification globale par (idOuv, site)",
        "max_emprunts": MAX_EMPRUNTS
    })
