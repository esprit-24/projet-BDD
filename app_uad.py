from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# 🔗 Connexion MySQL UAD
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",          # adapte si besoin
    database="site_uad"
)

@app.route("/etudiants", methods=["GET"])
def get_etudiants():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM etudiant_uad")
    etudiants = cursor.fetchall()
    return jsonify(etudiants)

@app.route("/ouvrages", methods=["GET"])
def get_ouvrages():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ouvrage_uad")
    return jsonify(cursor.fetchall())

@app.route("/prets", methods=["GET"])
def get_prets():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pret_uad")
    return jsonify(cursor.fetchall())

@app.route("/prets", methods=["POST"])
def ajouter_pret():
    data = request.json
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO pret_ugb (idOuv, idEtud, date_emprunt, date_retour)
        VALUES (%s, %s, %s, %s)
    """, (
        data["idOuv"],
        data["idEtud"],
        data["date_emprunt"],
        data["date_retour"]
    ))

    db.commit()
    return {"message": "Prêt ajouté à UAD"}, 201

@app.route("/")
def home():
    return "API UAD connectée à MySQL"

if __name__ == "__main__":
    app.run(port=5002)
