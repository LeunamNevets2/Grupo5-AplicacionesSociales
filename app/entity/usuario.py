import firebase_admin
from firebase_admin import credentials, firestore

class User:
    def __init__(self, user_id, nombre, email, telefono, tipo_usuario, fcm_token):
        self.user_id = user_id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.tipo_usuario = tipo_usuario
        self.fcm_token = fcm_token

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
            "tipo_usuario": self.tipo_usuario,
            "fcm_token": self.fcm_token,
            "fecha_creacion": firestore.SERVER_TIMESTAMP
        }
