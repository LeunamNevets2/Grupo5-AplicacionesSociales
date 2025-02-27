from dataaccess.comentario_dao import agregar_comentario, obtener_comentarios, eliminar_comentario

def agregar_comentario_bo(usuario_id, entidad_id, entidad_tipo, contenido):
    try:
        return agregar_comentario(usuario_id, entidad_id, entidad_tipo, contenido)
    except Exception as e:
        return {"error": "No se pudo agregar el comentario", "detalle": str(e)}

def obtener_comentarios_bo(entidad_id):
    try:
        return obtener_comentarios(entidad_id)
    except Exception as e:
        return {"error": "No se pudieron obtener los comentarios", "detalle": str(e)}

def eliminar_comentario_bo(comentario_id):
    try:
        return eliminar_comentario(comentario_id)
    except Exception as e:
        return {"error": "No se pudo eliminar el comentario", "detalle": str(e)}