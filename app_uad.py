from flask import Flask, request, jsonify
import psycopg2
import psycopg2.extras

app = Flask(__name__)

# 🔗 Connexion PostgreSQL UAD (Docker)
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        port=5433,
        database="site_uad",
        user="postgres",
        password="postgres"
    )

# ==========================
# Étudiants UAD
# ==========================
@app.route("/etudiants", methods=["GET"])
def get_etudiants():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("SELECT * FROM etudiant_uad")
    data = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(data)

@app.route("/etudiants/<int:idEtud>", methods=["GET"])
def get_etudiant_by_id(idEtud):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("SELECT * FROM etudiant_uad WHERE idEtud = %s", (idEtud,))
    etudiant = cur.fetchone()

    cur.close()
    conn.close()

    if etudiant:
        return jsonify(etudiant)
    return jsonify({"erreur": "Étudiant non trouvé"}), 404

# ==========================
# Ouvrages UAD
# ==========================
@app.route("/ouvrages", methods=["GET"])
def get_ouvrages():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("SELECT * FROM ouvrage_uad")
    data = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(data)

@app.route("/ouvrages/<int:idOuv>", methods=["GET"])
def get_ouvrage_by_id(idOuv):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("SELECT * FROM ouvrage_uad WHERE idOuv = %s", (idOuv,))
    ouvrage = cur.fetchone()

    cur.close()
    conn.close()

    if ouvrage:
        return jsonify(ouvrage)
    return jsonify({"erreur": "Ouvrage non trouvé"}), 404

# ==========================
# Prêts UAD
# ==========================
@app.route("/prets", methods=["GET"])
def get_prets():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute("SELECT * FROM pret_uad")
    data = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(data)

@app.route("/prets", methods=["POST"])
def ajouter_pret():
    data = request.json

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO pret_uad (idOuv, idEtud, date_emprunt, date_retour)
        VALUES (%s, %s, %s, %s)
    """, (
        data["idOuv"],
        data["idEtud"],
        data["date_emprunt"],
        data.get("date_retour")
    ))

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Prêt ajouté à UAD"}, 201

# ==========================
# Accueil
# ==========================
@app.route("/")
def home():
    return "API UAD connectée à PostgreSQL"

if __name__ == "__main__":
    app.run(port=5002, debug=True)
