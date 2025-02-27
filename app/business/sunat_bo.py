import uuid
from entity.sunatRuc import RespuestaSunat
from entity.sunatRucResponse import EmpresaDTO

def convertir_a_dto(empresa_api: RespuestaSunat) -> EmpresaDTO:
    return EmpresaDTO(
        resultado=empresa_api.success,
        ruc=empresa_api.ruc,
        nombre=empresa_api.nombre_o_razon_social,  # Corregimos este campo
        estado=empresa_api.estado_del_contribuyente,
        condicion=empresa_api.condicion_de_domicilio,
        direccion=empresa_api.direccion,
        distrito=empresa_api.distrito,
        provincia=empresa_api.provincia,
        departamento=empresa_api.departamento
    )