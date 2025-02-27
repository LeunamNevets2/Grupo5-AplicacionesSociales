import firebase_admin
from firebase_admin import credentials, firestore

class RespuestaSunat:
    def __init__(self, success=None, ruc=None, nombre_o_razon_social=None, estado_del_contribuyente=None, 
                 condicion_de_domicilio=None, ubigeo=None, tipo_de_via=None, nombre_de_via=None, 
                 codigo_de_zona=None, tipo_de_zona=None, numero=None, interior=None, lote=None, dpto=None, 
                 manzana=None, kilometro=None, distrito=None, provincia=None, departamento=None, 
                 direccion_simple=None, direccion=None, actualizado_en=None):
        self.success = success
        self.ruc = ruc
        self.nombre_o_razon_social = nombre_o_razon_social
        self.estado_del_contribuyente = estado_del_contribuyente
        self.condicion_de_domicilio = condicion_de_domicilio
        self.ubigeo = ubigeo
        self.tipo_de_via = tipo_de_via
        self.nombre_de_via = nombre_de_via
        self.codigo_de_zona = codigo_de_zona
        self.tipo_de_zona = tipo_de_zona
        self.numero = numero
        self.interior = interior
        self.lote = lote
        self.dpto = dpto
        self.manzana = manzana
        self.kilometro = kilometro
        self.distrito = distrito
        self.provincia = provincia
        self.departamento = departamento
        self.direccion_simple = direccion_simple
        self.direccion = direccion
        self.actualizado_en = actualizado_en

    def to_dict(self):
        return {
            "success": self.success,
            "ruc": self.ruc,
            "nombre_o_razon_social": self.nombre_o_razon_social,
            "estado_del_contribuyente": self.estado_del_contribuyente,
            "condicion_de_domicilio": self.condicion_de_domicilio,
            "ubigeo": self.ubigeo,
            "tipo_de_via": self.tipo_de_via,
            "nombre_de_via": self.nombre_de_via,
            "codigo_de_zona": self.codigo_de_zona,
            "tipo_de_zona": self.tipo_de_zona,
            "numero": self.numero,
            "interior": self.interior,
            "lote": self.lote,
            "dpto": self.dpto,
            "manzana": self.manzana,
            "distrito": self.distrito,
            "provincia": self.provincia,
            "departamento": self.departamento,
            "direccion_simple": self.direccion_simple,
            "direccion": self.direccion,
            "actualizado_en": self.actualizado_en
        }