import firebase_admin
from firebase_admin import credentials, firestore

class RespuestaSunatActividadRUC:
    def __init__(self, success=None, ruc=None, estado=None, condicion=None, tipo=None,
                 actividad_economica_rev3_principal=None, actividad_economica_rev3_secundaria=None,
                 actividad_economica_rev4_principal=None, numero_trabajadores=None,
                 tipo_facturacion=None, tipo_contabilidad=None, comercio_exterior=None,
                 periodo=None):
        self.success = success
        self.ruc = ruc
        self.estado = estado
        self.condicion = condicion
        self.tipo = tipo
        self.actividad_economica_rev3_principal = actividad_economica_rev3_principal
        self.actividad_economica_rev3_secundaria = actividad_economica_rev3_secundaria
        self.actividad_economica_rev4_principal = actividad_economica_rev4_principal
        self.numero_trabajadores = numero_trabajadores
        self.tipo_facturacion = tipo_facturacion
        self.tipo_contabilidad = tipo_contabilidad
        self.comercio_exterior = comercio_exterior
        self.periodo = periodo

def to_dict(self):
        return {
            "success": self.success,
            "ruc": self.ruc,
            "estado": self.estado,
            "condicion": self.condicion,
            "tipo": self.tipo,
            "actividad_economica_rev3_principal": self.actividad_economica_rev3_principal,
            "actividad_economica_rev3_secundaria": self.actividad_economica_rev3_secundaria,
            "actividad_economica_rev4_principal": self.actividad_economica_rev4_principal,
            "numero_trabajadores": self.numero_trabajadores,
            "tipo_facturacion": self.tipo_facturacion,
            "tipo_contabilidad": self.tipo_contabilidad,
            "comercio_exterior": self.comercio_exterior,
            "periodo": self.periodo
        }
