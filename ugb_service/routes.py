from flask import Blueprint, request, jsonify
from db import get_db_connection

ugb_routes = Blueprint("ugb_routes", __name__)

# ==========================
# Étudiants UGB
# ==========================
@ugb_routes.route("/etudiants", methods=["GET"])
def get_etudiants():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM etudiant_ugb")
        data = cur.fetchall()
    conn.close()
    return jsonify(data)

@ugb_routes.route("/etudiants/<int:idEtud>", methods=["GET"])
def get_etudiant_by_id(idEtud):
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM etudiant_ugb WHERE idEtud = %s",
            (idEtud,)
        )
        etudiant = cur.fetchone()
    conn.close()

    if etudiant:
        return jsonify(etudiant)
    return jsonify({"erreur": "Étudiant non trouvé"}), 404

# ==========================
# Étudiants emprunteurs
# ==========================
@ugb_routes.route("/etudiants/emprunteurs", methods=["GET"])
def get_etudiants_emprunteurs():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            SELECT DISTINCT e.*
            FROM etudiant_ugb e
            JOIN pret_ugb p ON e.idEtud = p.idEtud
        """)
        data = cur.fetchall()
    conn.close()
    return jsonify(data)

# ==========================
# Ouvrages UGB
# ==========================
@ugb_routes.route("/ouvrages", methods=["GET"])
def get_ouvrages():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM ouvrage_ugb")
        data = cur.fetchall()
    conn.close()
    return jsonify(data)

# ==========================
# Prêts UGB (AVEC gestion du stock)
# ==========================
@ugb_routes.route("/prets", methods=["POST"])
def ajouter_pret():
    data = request.json
    conn = get_db_connection()

    try:
        with conn.cursor() as cur:
            # 🔒 Vérifier stock
            cur.execute(
                "SELECT stock FROM ouvrage_ugb WHERE idOuv = %s",
                (data["idOuv"],)
            )
            ouvrage = cur.fetchone()
            if not ouvrage or ouvrage["stock"] <= 0:
                return jsonify({"erreur": "Ouvrage indisponible"}), 409

            # ➕ Insérer prêt
            cur.execute("""
                INSERT INTO pret_ugb (idOuv, idEtud, date_emprunt, date_retour)
                VALUES (%s, %s, %s, %s)
            """, (
                data["idOuv"],
                data["idEtud"],
                data["date_emprunt"],
                data.get("date_retour")
            ))

            # ➖ Décrémenter stock
            cur.execute("""
                UPDATE ouvrage_ugb
                SET stock = stock - 1
                WHERE idOuv = %s
            """, (data["idOuv"],))

            # ➕ Incrémenter emprunts étudiant
            cur.execute("""
                UPDATE etudiant_ugb
                SET nbreEmprunts = nbreEmprunts + 1
                WHERE idEtud = %s
            """, (data["idEtud"],))

        conn.commit()
        return jsonify({"message": "Prêt ajouté à UGB"}), 201

    except Exception as e:
        conn.rollback()
        return jsonify({"erreur": str(e)}), 500

    finally:
        conn.close()

# ==========================
# Accueil
# ==========================
@ugb_routes.route("/")
def home():
    return "API UGB connectée à MySQL (service UGB)"
