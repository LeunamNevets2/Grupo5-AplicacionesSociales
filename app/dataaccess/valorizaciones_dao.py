from app.dataaccess.firebase_db import db

def agregar_valorizacion(ruc, id_usuario, estrellas):
    """Guarda una valoración de una empresa en Firestore."""
    try:
        nueva_valorizacion = {
            "ruc": ruc,
            "id_usuario": id_usuario,
            "estrellas": estrellas
        }
        db.collection("valorizacionesEmpresas").add(nueva_valorizacion)
        return True
    except Exception as e:
        return {"error": "No se pudo guardar la valorización", "detalle": str(e)}

def obtener_promedio_valorizaciones(ruc):
    """Calcula el promedio de las valoraciones para una empresa según su RUC."""
    try:
        valoraciones = db.collection("valorizacionesEmpresas").where("ruc", "==", ruc).stream()
        
        total_estrellas = 0
        total_valoraciones = 0

        for valoracion in valoraciones:
            total_estrellas += valoracion.to_dict().get("estrellas", 0)
            total_valoraciones += 1

        if total_valoraciones == 0:
            return {"mensaje": "No hay valoraciones para este RUC", "promedio": None}

        promedio = total_estrellas / total_valoraciones
        return {"ruc": ruc, "promedio": round(promedio, 2)}

    except Exception as e:
        return {"error": "No se pudo calcular el promedio", "detalle": str(e)}