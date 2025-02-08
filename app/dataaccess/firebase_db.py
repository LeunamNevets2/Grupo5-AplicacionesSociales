import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase con credenciales
cred = credentials.Certificate("evaluared-appsocial-firebase-adminsdk-fbsvc-1a6e2690de.json")
firebase_admin.initialize_app(cred)

# Conectar con Firestore
db = firestore.client()
