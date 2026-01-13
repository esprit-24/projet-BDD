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
# Étudiants ayant fait des emprunts
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

@uad_routes.route("/ouvrages/<int:idOuv>", methods=["GET"])
def get_ouvrage_by_id(idOuv):
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
        WHERE idOuv = %s
    """, (idOuv,))
    ouvrage = cur.fetchone()

    cur.close()
    conn.close()

    if ouvrage:
        return jsonify(ouvrage)
    return jsonify({"erreur": "Ouvrage non trouvé"}), 404

# ==========================
# Prêts UAD
# ==========================
@uad_routes.route("/prets", methods=["GET"])
def get_prets():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("""
        SELECT
            idOuv         AS "idOuv",
            idEtud        AS "idEtud",
            date_emprunt  AS "date_emprunt",
            date_retour   AS "date_retour"
        FROM pret_uad
    """)
    data = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(data)

@uad_routes.route("/prets", methods=["POST"])
def ajouter_pret():
    data = request.json

    conn = get_db_connection()
    cur = conn.cursor()

    id_ouv = data.get("idOuv") or data.get("idouv")
    id_etud = data.get("idEtud") or data.get("idetud")

    cur.execute("""
        INSERT INTO pret_uad (idOuv, idEtud, date_emprunt, date_retour)
        VALUES (%s, %s, %s, %s)
    """, (
        id_ouv,
        id_etud,
        data["date_emprunt"],
        data.get("date_retour")
    ))

    # Mise à jour du nombre d’emprunts (exigence du sujet)
    cur.execute("""
        UPDATE etudiant_uad
        SET nbreEmprunts = nbreEmprunts + 1
        WHERE idEtud = %s
    """, (id_etud,))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Prêt ajouté à UAD"}), 201

# ==========================
# Accueil
# ==========================
@uad_routes.route("/")
def home():
    return "API UAD connectée à PostgreSQL (service UAD)"
