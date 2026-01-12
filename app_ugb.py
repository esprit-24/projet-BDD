from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# 🔗 Connexion MySQL UGB (Docker) — PyMySQL
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        port=3307,
        user="root",
        password="root",
        database="site_ugb",
        cursorclass=pymysql.cursors.DictCursor
    )

# ==========================
# Test API
# ==========================
@app.route("/test")
def test():
    return "UGB API OK"

# ==========================
# Étudiants UGB
# ==========================
@app.route("/etudiants", methods=["GET"])
def get_etudiants():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM etudiant_ugb")
        data = cur.fetchall()
    conn.close()
    return jsonify(data)

@app.route("/etudiants/<int:idEtud>", methods=["GET"])
def get_etudiant_by_id(idEtud):
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM etudiant_ugb WHERE idEtud = %s", (idEtud,))
        etudiant = cur.fetchone()
    conn.close()

    if etudiant:
        return jsonify(etudiant)
    return jsonify({"erreur": "Étudiant non trouvé"}), 404

# ==========================
# Ouvrages UGB
# ==========================
@app.route("/ouvrages", methods=["GET"])
def get_ouvrages():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM ouvrage_ugb")
        data = cur.fetchall()
    conn.close()
    return jsonify(data)

@app.route("/ouvrages/<int:idOuv>", methods=["GET"])
def get_ouvrage_by_id(idOuv):
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM ouvrage_ugb WHERE idOuv = %s", (idOuv,))
        ouvrage = cur.fetchone()
    conn.close()

    if ouvrage:
        return jsonify(ouvrage)
    return jsonify({"erreur": "Ouvrage non trouvé"}), 404

# ==========================
# Prêts UGB
# ==========================
@app.route("/prets", methods=["GET"])
def get_prets():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM pret_ugb")
        data = cur.fetchall()
    conn.close()
    return jsonify(data)

@app.route("/prets", methods=["POST"])
def ajouter_pret():
    data = request.json
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO pret_ugb (idOuv, idEtud, date_emprunt, date_retour)
            VALUES (%s, %s, %s, %s)
        """, (
            data["idOuv"],
            data["idEtud"],
            data["date_emprunt"],
            data.get("date_retour")
        ))
        conn.commit()
    conn.close()
    return {"message": "Prêt ajouté à UGB"}, 201

# ==========================
# Accueil
# ==========================
@app.route("/")
def home():
    return "API UGB connectée à MySQL (PyMySQL)"

if __name__ == "__main__":
    app.run(port=5001, debug=False, use_reloader=False)
