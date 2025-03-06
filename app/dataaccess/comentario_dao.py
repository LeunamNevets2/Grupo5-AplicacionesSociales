from app.dataaccess.firebase_db import db
from datetime import datetime
from google.cloud import firestore
import pytz

def agregar_comentario(usuario_id, entidad_id, entidad_tipo, contenido):
    comentario_ref = db.collection("comentarios").document()
    comentario_data = {
        "id": comentario_ref.id,
        "usuario_id": usuario_id,
        "entidad_id": entidad_id,
        "entidad_tipo": entidad_tipo,
        "contenido": contenido,
        "fecha_creacion": firestore.SERVER_TIMESTAMP
    }
    
    comentario_ref.set(comentario_data)

    # Recuperar el comentario ya almacenado con el timestamp procesado
    comentario_guardado = comentario_ref.get().to_dict()

    # Convertir timestamp a UTC-5
    if "fecha_creacion" in comentario_guardado and comentario_guardado["fecha_creacion"]:
        utc_time = comentario_guardado["fecha_creacion"].replace(tzinfo=pytz.utc)  # Asegurar que es UTC
        lima_time = utc_time.astimezone(pytz.timezone("America/Lima"))  # Convertir a UTC-5
        comentario_guardado["fecha_creacion"] = lima_time.isoformat()

    return comentario_guardado

def obtener_comentarios(entidad_id):
    comentarios = db.collection("comentarios") \
                    .where("entidad_id", "==", entidad_id) \
                    .stream()  # <-- Sin ordenamiento
    
    return [coment.to_dict() for coment in comentarios]

def eliminar_comentario(comentario_id):
    comentario_ref = db.collection("comentarios").document(comentario_id)
    comentario_ref.delete()
    return {"mensaje": "Comentario eliminado"}