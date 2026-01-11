from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from functools import wraps
import logging
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Permet les requêtes depuis le navigateur

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

UGB = "http://127.0.0.1:5001"
UAD = "http://127.0.0.1:5002"

# Timeout pour les requêtes
REQUEST_TIMEOUT = 5


# ======================================================
# Décorateur pour gérer les erreurs
# ======================================================
def handle_errors(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except requests.exceptions.Timeout:
            logger.error(f"Timeout lors de l'appel à {f.__name__}")
            return jsonify({"erreur": "Délai d'attente dépassé"}), 504
        except requests.exceptions.ConnectionError:
            logger.error(f"Erreur de connexion dans {f.__name__}")
            return jsonify({"erreur": "Service indisponible"}), 503
        except Exception as e:
            logger.error(f"Erreur dans {f.__name__}: {str(e)}")
            return jsonify({"erreur": str(e)}), 500
    return decorated_function


# ======================================================
# Fonction helper pour les requêtes
# ======================================================
def safe_request(method, url, **kwargs):
    """Effectue une requête avec gestion d'erreurs"""
    try:
        kwargs['timeout'] = REQUEST_TIMEOUT
        response = requests.request(method, url, **kwargs)
        
        # Log la réponse même en cas d'erreur
        if response.status_code >= 400:
            logger.error(f"Erreur {response.status_code} de {url}")
            logger.error(f"Réponse: {response.text}")
        
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur requête {method} {url}: {str(e)}")
        raise


# ======================================================
# 1️⃣ Tous les étudiants (toutes universités)
# ======================================================
@app.route("/etudiants", methods=["GET"])
@handle_errors
def get_all_etudiants():
    logger.info("Récupération de tous les étudiants")
    
    resultat = {}
    for nom, base in [("UGB", UGB), ("UAD", UAD)]:
        try:
            r = safe_request("GET", f"{base}/etudiants")
            resultat[nom] = r.json()
        except Exception as e:
            logger.warning(f"Impossible de récupérer les étudiants de {nom}")
            resultat[nom] = {"erreur": str(e)}
    
    return jsonify(resultat)


# ======================================================
# 2️⃣ Faire un emprunt
# ======================================================
@app.route("/emprunt", methods=["POST"])
@handle_errors
def faire_emprunt():
    data = request.json
    
    # Validation des données
    if not data:
        return jsonify({"erreur": "Données manquantes"}), 400
    
    universite = data.get("universite")
    id_etud = data.get("idEtud")
    id_ouv = data.get("idOuv")
    date_emprunt = data.get("dateEmprunt")
    
    # Validation des champs requis
    if not all([universite, id_etud, id_ouv, date_emprunt]):
        return jsonify({"erreur": "Tous les champs sont requis"}), 400
    
    logger.info(f"Création emprunt: étudiant {id_etud}, ouvrage {id_ouv}, {universite}")
    logger.info(f"Données envoyées: {data}")
    
    # Préparer les données au format attendu par les serveurs universitaires
    # Utiliser snake_case (date_emprunt) au lieu de camelCase (dateEmprunt)
    data_to_send = {
        "id_etud": id_etud,
        "id_ouv": id_ouv,
        "date_emprunt": date_emprunt
    }
    
    if universite == "UGB":
        r = safe_request("POST", f"{UGB}/prets", json=data_to_send)
    elif universite == "UAD":
        r = safe_request("POST", f"{UAD}/prets", json=data_to_send)
    else:
        return jsonify({"erreur": "Université invalide (UGB ou UAD)"}), 400
    
    return jsonify(r.json()), r.status_code


# ======================================================
# 3️⃣ Étudiants ayant fait au moins un emprunt
# ======================================================
@app.route("/etudiants/emprunteurs", methods=["GET"])
@handle_errors
def etudiants_emprunteurs():
    logger.info("Récupération des étudiants emprunteurs")
    resultat = {}
    
    for nom, base in [("UGB", UGB), ("UAD", UAD)]:
        try:
            etudiants = safe_request("GET", f"{base}/etudiants").json()
            prets = safe_request("GET", f"{base}/prets").json()
            
            ids = {p["idEtud"] for p in prets}
            resultat[nom] = [e for e in etudiants if e["idEtud"] in ids]
        except Exception as e:
            logger.warning(f"Erreur pour {nom}: {str(e)}")
            resultat[nom] = []
    
    return jsonify(resultat)


# ======================================================
# 4️⃣ Tous les emprunts
# ======================================================
@app.route("/emprunts", methods=["GET"])
@handle_errors
def tous_les_emprunts():
    logger.info("Récupération de tous les emprunts")
    
    resultat = {}
    for nom, base in [("UGB", UGB), ("UAD", UAD)]:
        try:
            r = safe_request("GET", f"{base}/prets")
            resultat[nom] = r.json()
        except Exception as e:
            logger.warning(f"Impossible de récupérer les emprunts de {nom}")
            resultat[nom] = []
    
    return jsonify(resultat)


# ======================================================
# 5️⃣ Emprunts d'un étudiant (par id)
# ======================================================
@app.route("/emprunts/etudiant/<int:idEtud>", methods=["GET"])
@handle_errors
def emprunts_par_etudiant(idEtud):
    logger.info(f"Récupération des emprunts pour l'étudiant {idEtud}")
    resultat = {}
    
    for nom, base in [("UGB", UGB), ("UAD", UAD)]:
        try:
            prets = safe_request("GET", f"{base}/prets").json()
            resultat[nom] = [p for p in prets if p["idEtud"] == idEtud]
        except Exception as e:
            logger.warning(f"Erreur pour {nom}: {str(e)}")
            resultat[nom] = []
    
    return jsonify(resultat)


# ======================================================
# 6️⃣ Vérifier si un étudiant peut emprunter
# ======================================================
@app.route("/emprunt/verifier/<int:idEtud>", methods=["GET"])
@handle_errors
def verifier_emprunt(idEtud):
    logger.info(f"Vérification emprunt pour étudiant {idEtud}")
    
    for nom, base in [("UGB", UGB), ("UAD", UAD)]:
        try:
            prets = safe_request("GET", f"{base}/prets").json()
            if any(p["idEtud"] == idEtud for p in prets):
                return jsonify({
                    "autorise": False,
                    "message": f"Étudiant a déjà un emprunt ({nom})",
                    "universite": nom
                })
        except Exception as e:
            logger.warning(f"Erreur vérification pour {nom}: {str(e)}")
    
    return jsonify({
        "autorise": True,
        "message": "Étudiant peut emprunter"
    })


# ======================================================
# 7️⃣ Ouvrages disponibles par université
# ======================================================
@app.route("/ouvrages/disponibles", methods=["GET"])
@handle_errors
def ouvrages_disponibles():
    logger.info("Récupération des ouvrages disponibles")
    resultat = {}
    
    for nom, base in [("UGB", UGB), ("UAD", UAD)]:
        try:
            ouvrages = safe_request("GET", f"{base}/ouvrages").json()
            prets = safe_request("GET", f"{base}/prets").json()
            
            ouvrages_empruntes = {p["idOuv"] for p in prets}
            resultat[nom] = [
                o for o in ouvrages if o["idOuv"] not in ouvrages_empruntes
            ]
        except Exception as e:
            logger.warning(f"Erreur pour {nom}: {str(e)}")
            resultat[nom] = []
    
    return jsonify(resultat)


# ======================================================
# 8️⃣ Tous les ouvrages
# ======================================================
@app.route("/ouvrages", methods=["GET"])
@handle_errors
def tous_les_ouvrages():
    logger.info("Récupération de tous les ouvrages")
    
    resultat = {}
    for nom, base in [("UGB", UGB), ("UAD", UAD)]:
        try:
            r = safe_request("GET", f"{base}/ouvrages")
            resultat[nom] = r.json()
        except Exception as e:
            logger.warning(f"Impossible de récupérer les ouvrages de {nom}")
            resultat[nom] = []
    
    return jsonify(resultat)


# ======================================================
# 9️⃣ Statistiques globales
# ======================================================
@app.route("/statistiques", methods=["GET"])
@handle_errors
def statistiques():
    logger.info("Calcul des statistiques globales")
    stats = {
        "UGB": {"etudiants": 0, "emprunts": 0, "ouvrages": 0, "disponibles": 0},
        "UAD": {"etudiants": 0, "emprunts": 0, "ouvrages": 0, "disponibles": 0}
    }
    
    for nom, base in [("UGB", UGB), ("UAD", UAD)]:
        try:
            etudiants = safe_request("GET", f"{base}/etudiants").json()
            prets = safe_request("GET", f"{base}/prets").json()
            ouvrages = safe_request("GET", f"{base}/ouvrages").json()
            
            ouvrages_empruntes = {p["idOuv"] for p in prets}
            
            stats[nom] = {
                "etudiants": len(etudiants),
                "emprunts": len(prets),
                "ouvrages": len(ouvrages),
                "disponibles": len([o for o in ouvrages if o["idOuv"] not in ouvrages_empruntes])
            }
        except Exception as e:
            logger.warning(f"Erreur statistiques pour {nom}: {str(e)}")
    
    stats["total"] = {
        "etudiants": stats["UGB"]["etudiants"] + stats["UAD"]["etudiants"],
        "emprunts": stats["UGB"]["emprunts"] + stats["UAD"]["emprunts"],
        "ouvrages": stats["UGB"]["ouvrages"] + stats["UAD"]["ouvrages"],
        "disponibles": stats["UGB"]["disponibles"] + stats["UAD"]["disponibles"]
    }
    
    return jsonify(stats)


# ======================================================
# 🔟 Health check (vérification de santé)
# ======================================================
@app.route("/health", methods=["GET"])
def health_check():
    status = {
        "service": "Bibliothèque Universitaire",
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "universities": {}
    }
    
    for nom, base in [("UGB", UGB), ("UAD", UAD)]:
        try:
            r = requests.get(f"{base}/etudiants", timeout=2)
            status["universities"][nom] = "online" if r.status_code == 200 else "offline"
        except:
            status["universities"][nom] = "offline"
    
    return jsonify(status)


# ======================================================
# Accueil avec documentation
# ======================================================
@app.route("/")
def home():
    return jsonify({
        "service": "Micro-service Bibliothèque Universitaire",
        "version": "2.0",
        "status": "opérationnel",
        "endpoints": {
            "GET /etudiants": "Liste tous les étudiants",
            "GET /etudiants/emprunteurs": "Étudiants ayant emprunté",
            "POST /emprunt": "Créer un emprunt",
            "GET /emprunts": "Liste tous les emprunts",
            "GET /emprunts/etudiant/<id>": "Emprunts d'un étudiant",
            "GET /emprunt/verifier/<id>": "Vérifier si étudiant peut emprunter",
            "GET /ouvrages": "Liste tous les ouvrages",
            "GET /ouvrages/disponibles": "Ouvrages disponibles",
            "GET /statistiques": "Statistiques globales",
            "GET /health": "État de santé du service"
        }
    })


# ======================================================
# Gestionnaire d'erreurs 404
# ======================================================
@app.errorhandler(404)
def not_found(error):
    return jsonify({"erreur": "Endpoint non trouvé"}), 404


# ======================================================
# Gestionnaire d'erreurs 500
# ======================================================
@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Erreur serveur: {str(error)}")
    return jsonify({"erreur": "Erreur interne du serveur"}), 500


if __name__ == "__main__":
    logger.info("Démarrage du micro-service Bibliothèque Universitaire")
    app.run(host='0.0.0.0', port=5000, debug=True)