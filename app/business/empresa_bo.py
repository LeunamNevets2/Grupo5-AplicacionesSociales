# business/empresa_service.py
import uuid
from app.entity.empresa import Empresa
from app.dataaccess.empresa_dao import registrar_empresa

def crear_empresa(nombre, ruc, direccion, telefono, categoria, propietario_id, validada_sunat):
    empresa_id = str(uuid.uuid4())  # Generar un ID único
    nueva_empresa = Empresa(empresa_id, nombre, ruc, direccion, telefono, categoria, propietario_id, validada_sunat)
    return registrar_empresa(nueva_empresa)
