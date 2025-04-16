import json

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

def handler(request):
    query = request.get("queryStringParameters") or {}
    adresse = (query.get("adresse") or "").strip().lower()
    result = dpe_data.get(adresse)

    if result:
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"status": "trouvé", "dpe": result})
        }
    else:
        return {
            "statusCode": 404,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"status": "non_trouvé", "message": "Aucun DPE connu pour cette adresse."})
        }
