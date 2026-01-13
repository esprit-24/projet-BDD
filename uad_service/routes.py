from flask import Blueprint, request, jsonify
from db import get_db_connection
import psycopg2.extras

uad_routes = Blueprint("uad_routes", __name__)

# ==========================
# Étudiants UAD
# ==========================
@uad_routes.route("/etudiants", methods=["GET"])
def get_etudiants():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("""
        SELECT
            idEtud        AS "idEtud",
            nom           AS "nom",
            adresse       AS "adresse",
            universite    AS "universite",
            specialite    AS "specialite",
            nbreEmprunts  AS "nbreEmprunts"
        FROM etudiant_uad
    """)
    data = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(data)

@uad_routes.route("/etudiants/<int:idEtud>", methods=["GET"])
def get_etudiant_by_id(idEtud):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("""
        SELECT
            idEtud        AS "idEtud",
            nom           AS "nom",
            adresse       AS "adresse",
            universite    AS "universite",
            specialite    AS "specialite",
            nbreEmprunts  AS "nbreEmprunts"
        FROM etudiant_uad
        WHERE idEtud = %s
    """, (idEtud,))
    etudiant = cur.fetchone()

    cur.close()
    conn.close()

    if etudiant:
        return jsonify(etudiant)
    return jsonify({"erreur": "Étudiant non trouvé"}), 404

# ==========================
# Étudiants emprunteurs
# ==========================
@uad_routes.route("/etudiants/emprunteurs", methods=["GET"])
def get_etudiants_emprunteurs():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("""
        SELECT DISTINCT
            e.idEtud       AS "idEtud",
            e.nom          AS "nom",
            e.adresse      AS "adresse",
            e.universite   AS "universite",
            e.specialite   AS "specialite",
            e.nbreEmprunts AS "nbreEmprunts"
        FROM etudiant_uad e
        JOIN pret_uad p ON e.idEtud = p.idEtud
    """)
    data = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(data)

# ==========================
# Ouvrages UAD
# ==========================
@uad_routes.route("/ouvrages", methods=["GET"])
def get_ouvrages():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("""
        SELECT
            idOuv    AS "idOuv",
            titre    AS "titre",
            idAut    AS "idAut",
            editeur  AS "editeur",
            annee    AS "annee",
            domaine  AS "domaine",
            stock    AS "stock",
            site     AS "site"
        FROM ouvrage_uad
    """)
    data = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(data)

# ==========================
# Prêts UAD (AVEC gestion du stock)
# ==========================
@uad_routes.route("/prets", methods=["POST"])
def ajouter_pret():
    data = request.json
    conn = get_db_connection()

    try:
        cur = conn.cursor()

        id_ouv = data["idOuv"]
        id_etud = data["idEtud"]

        # 🔒 Vérifier stock
        cur.execute(
            "SELECT stock FROM ouvrage_uad WHERE idOuv = %s",
            (id_ouv,)
        )
        res = cur.fetchone()
        if not res or res[0] <= 0:
            return jsonify({"erreur": "Ouvrage indisponible"}), 409

        # ➕ Insérer prêt
        cur.execute("""
            INSERT INTO pret_uad (idOuv, idEtud, date_emprunt, date_retour)
            VALUES (%s, %s, %s, %s)
        """, (
            id_ouv,
            id_etud,
            data["date_emprunt"],
            data.get("date_retour")
        ))

        # ➖ Décrémenter stock
        cur.execute("""
            UPDATE ouvrage_uad
            SET stock = stock - 1
            WHERE idOuv = %s
        """, (id_ouv,))

        # ➕ Incrémenter emprunts étudiant
        cur.execute("""
            UPDATE etudiant_uad
            SET nbreEmprunts = nbreEmprunts + 1
            WHERE idEtud = %s
        """, (id_etud,))

        conn.commit()
        return jsonify({"message": "Prêt ajouté à UAD"}), 201

    except Exception as e:
        conn.rollback()
        return jsonify({"erreur": str(e)}), 500

    finally:
        cur.close()
        conn.close()

# ==========================
# Accueil
# ==========================
@uad_routes.route("/")
def home():
    return "API UAD connectée à PostgreSQL (service UAD)"
