from datetime import datetime
from google.cloud import firestore

class Comentario:
    def __init__(self, id, usuario_id, entidad_id, entidad_tipo, contenido, fecha_creacion=None):
        self.id = id  # Identificador único
        self.usuario_id = usuario_id  # Usuario que hace el comentario
        self.entidad_id = entidad_id  # ID de la empresa/publicación/comentario al que se responde
        self.entidad_tipo = entidad_tipo  # Tipo de entidad comentada (empresa, post, etc.)
        self.contenido = contenido  # Texto del comentario
        self.fecha_creacion = fecha_creacion or firestore.SERVER_TIMESTAMP  # Fecha de creación

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "entidad_id": self.entidad_id,
            "entidad_tipo": self.entidad_tipo,
            "contenido": self.contenido,
            "fecha_creacion": self.fecha_creacion
        }