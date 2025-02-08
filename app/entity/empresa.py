import firebase_admin
from firebase_admin import credentials, firestore

class Empresa:
    def __init__(self, empresa_id, nombre, ruc, direccion, telefono, categoria, propietario_id, validada_sunat):
        self.empresa_id = empresa_id
        self.nombre = nombre
        self.ruc = ruc
        self.direccion = direccion
        self.telefono = telefono
        self.categoria = categoria
        self.propietario_id = propietario_id
        self.validada_sunat = validada_sunat

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "ruc": self.ruc,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "categoria": self.categoria,
            "propietario_id": self.propietario_id,
            "validada_sunat": self.validada_sunat,
            "fecha_registro": firestore.SERVER_TIMESTAMP
        }