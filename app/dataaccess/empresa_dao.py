# dataaccess/empresa_dao.py
from dataaccess.firebase_db import db

def registrar_empresa(empresa):
    doc_ref = db.collection("empresas").document(empresa.empresa_id)
    doc_ref.set(empresa.to_dict())
    return {"message": "Empresa registrada correctamente", "empresa_id": empresa.empresa_id}
