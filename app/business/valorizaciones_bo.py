from dataaccess.valorizaciones_dao import agregar_valorizacion, obtener_promedio_valorizaciones

def agregar_valorizacion_bo(ruc, id_usuario, estrellas):
    """Lógica de negocio para agregar una valorización."""
    try:
        if not (1 <= estrellas <= 5):
            return {"error": "Las estrellas deben estar entre 1 y 5"}
        
        return agregar_valorizacion(ruc, id_usuario, estrellas)
    except Exception as e:
        return {"error": "No se pudo agregar la valorización", "detalle": str(e)}

def obtener_promedio_valorizaciones_bo(ruc):
    """Lógica de negocio para calcular el promedio de las valorizaciones de una empresa."""
    try:
        return obtener_promedio_valorizaciones(ruc)
    except Exception as e:
        return {"error": "No se pudo obtener el promedio", "detalle": str(e)}