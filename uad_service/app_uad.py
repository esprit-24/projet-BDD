from flask import Flask
from routes import uad_routes

app = Flask(__name__)

# Enregistrement des routes UAD
app.register_blueprint(uad_routes)

if __name__ == "__main__":
    app.run(port=5002, debug=False, use_reloader=False)
