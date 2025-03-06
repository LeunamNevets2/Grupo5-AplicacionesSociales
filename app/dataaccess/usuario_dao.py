# dataaccess/user_dao.py
from app.dataaccess.firebase_db import db

def registrar_usuario(user):
    doc_ref = db.collection("usuarios").document(user.user_id)
    doc_ref.set(user.to_dict())
    return {"message": "Usuario registrado correctamente", "user_id": user.user_id}