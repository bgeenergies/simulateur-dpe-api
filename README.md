# Simulateur DPE - API

Cette API permet de simuler un Diagnostic de Performance Énergétique (DPE) à partir de données saisies par l'utilisateur. Elle est conçue pour être facilement déployée sur Vercel en utilisant les fonctions serverless de type Python.

## 🔧 Fonctionnalités

- Calcul du DPE selon des critères prédéfinis
- Réponse structurée en JSON
- Déploiement facile via Vercel

## 📁 Structure du projet

## 🚀 Déploiement sur Vercel

1. Connectez ce dépôt à [Vercel](https://vercel.com/)
2. Vercel détectera automatiquement la configuration `vercel.json`
3. Le fichier `api/api_dpe.py` sera traité comme une fonction serverless

⚠️ N'oubliez pas de choisir **Python** comme environnement si nécessaire.

## 📦 Installation locale

```bash
# Cloner le repo
git clone https://github.com/bgenergies/simulateur-dpe-api.git
cd simulateur-dpe-api

# Installer les dépendances
pip install -r requirements.txt

# Lancer un serveur local (ex: avec Flask, FastAPI, etc.)
# Assurez-vous que le fichier api_dpe.py contient un handler adapté
POST /api/api_dpe.py HTTP/1.1
Host: your-vercel-url.vercel.app
Content-Type: application/json

{
  "surface": 90,
  "type_energie": "gaz",
  "isolation": "bonne"
}
{
  "classe_dpe": "C",
  "consommation_energie": 110,
  "emissions_co2": 12
}

---

👉 Tu peux bien sûr adapter le contenu aux paramètres réels de ton API si certains détails changent (comme les noms de champs JSON, ou les niveaux de DPE).

Si tu veux que je t’aide à générer le `api_dpe.py` ou à tester tout ça sur Vercel, je suis là !

