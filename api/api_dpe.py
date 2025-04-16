from flask import Flask, request, jsonify

app = Flask(__name__)

# Base DPE simulée avec chauffage
dpe_data = {
    "12 rue victor hugo, 75000 paris": {
        "etiquette_energie": "D",
        "etiquette_climat": "C",
        "chauffage": "Gaz naturel"
    },
    "5 avenue des champs elysees, 75008 paris": {
        "etiquette_energie": "C",
        "etiquette_climat": "B",
        "chauffage": "Pompe à chaleur"
    },
    "17 boulevard haussmann, 75009 paris": {
        "etiquette_energie": "B",
        "etiquette_climat": "A",
        "chauffage": "Electricité"
    }
}

@app.route("/api/dpe", methods=["GET"])
def get_dpe():
    adresse = request.args.get("adresse", "").strip().lower()
    result = dpe_data.get(adresse)
    if result:
        return jsonify({"status": "trouvé", "dpe": result})
    else:
        return jsonify({"status": "non_trouvé", "message": "Aucun DPE connu pour cette adresse."}), 404