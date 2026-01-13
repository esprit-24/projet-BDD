from flask import Flask
from routes import ugb_routes

app = Flask(__name__)

# Enregistrement des routes UGB
app.register_blueprint(ugb_routes)

if __name__ == "__main__":
    app.run(port=5001, debug=False, use_reloader=False)
