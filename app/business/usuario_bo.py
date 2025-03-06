# business/user_service.py
import uuid
from app.entity.usuario import User
from app.dataaccess.usuario_dao import registrar_usuario

def crear_usuario(nombre, email, telefono, tipo_usuario, fcm_token):
    user_id = str(uuid.uuid4())  # Generar un ID único
    nuevo_usuario = User(user_id, nombre, email, telefono, tipo_usuario, fcm_token)
    return registrar_usuario(nuevo_usuario)
