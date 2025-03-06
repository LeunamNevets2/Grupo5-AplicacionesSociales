import requests
from flask import Blueprint, request, jsonify
from app.business.usuario_bo import crear_usuario
from app.business.empresa_bo import crear_empresa
from app.business.sunat_bo import convertir_a_dto
from app.entity.sunatRuc import RespuestaSunat
from app.entity.sunatActividadRuc import RespuestaSunatActividadRUC
from app.entity.sunatRepresentanteLegal import SunatRepresentanteLegalResponse
from app.business.comentario_bo import agregar_comentario_bo, obtener_comentarios_bo, eliminar_comentario_bo
from app.business.valorizaciones_bo import agregar_valorizacion_bo, obtener_promedio_valorizaciones_bo


API_URL_EMPRESA = "https://api.migo.pe/api/v1/ruc"
API_URL_REPRESENTANTE_LEGAL = "https://api.migo.pe/api/v1/ruc/representantes-legales"
API_URL_ACTIVIDAD = "https://api.migo.pe/api/v1/ruc/actividad/{}?token={}"
API_TOKEN = "HwmzUgPStEVSsZ3P19zyYEk8UeA1rDFkIDuJWdg5BOKlJYj47vH0wIhFHr6l" 

routes = Blueprint("routes", __name__)

# Endpoint para registrar usuario
@routes.route("/registro/usuario", methods=["POST"])
def registro_usuario():
    data = request.json
    resultado = crear_usuario(data["nombre"], data["email"], data["telefono"], data["tipo_usuario"], data.get("fcm_token", ""))
    return jsonify(resultado)

# Endpoint para registrar empresa
@routes.route("/registro/empresa", methods=["POST"])
def registro_empresa():
    data = request.json
    resultado = crear_empresa(data["nombre"], data["ruc"], data["direccion"], data["telefono"], data["categoria"], data["propietario_id"], data["validada_sunat"])
    return jsonify(resultado)

#Endpoints para obtener datos de la SUNAT por ruc
@routes.route('/sunatData/verificarRuc', methods=['POST'])
def obtener_empresa():
    # Extraer el RUC del cuerpo de la solicitud
    req_data = request.get_json()
    if not req_data or "ruc" not in req_data:
        return jsonify({"error": "Se requiere el RUC"}), 400    

    ruc = req_data["ruc"]

    # Agregar el token en el cuerpo de la solicitud
    payload = {
        "token": API_TOKEN,  # Pasamos el token en el JSON
        "ruc": ruc
    }

    response = requests.post(API_URL_EMPRESA, json=payload)

    if response.status_code == 200:
        data = response.json()
        empresa_api = RespuestaSunat(**data)
        empresa_dto = convertir_a_dto(empresa_api)
        return jsonify(empresa_dto.__dict__)
    else:
        return jsonify({"error": "No se encontró la empresa"}), response.status_code

#Endpoints para obtener datos de la actividad en SUNAT por ruc
@routes.route('/sunatData/verificarRuc/actividad', methods=['POST'])
def obtener_actividad_ruc():
    """
    Endpoint para obtener la actividad económica de una empresa según su RUC.
    
    :return: JSON con la información de la empresa o un mensaje de error.
    """
    req_data = request.get_json()

    if not req_data or "ruc" not in req_data:
        return jsonify({"error": "Se requiere el RUC en el cuerpo de la solicitud"}), 400
    
    ruc = req_data["ruc"]
    url = API_URL_ACTIVIDAD.format(ruc, API_TOKEN)

    print(f"🔍 URL generada: {url}")  # Imprime la URL en la consola

    try:
        response = requests.get(url)

        print(f"📡 Código de estado: {response.status_code}")  # Muestra el código de respuesta
        print(f"📄 Respuesta: {response.text}")  # Imprime el contenido de la respuesta en la consola

        if response.status_code == 200:
            data = response.json()
            actividad_ruc = RespuestaSunatActividadRUC(**data)
            return jsonify(actividad_ruc.__dict__)  # Convertir la respuesta en JSON
        else:
            return jsonify({"error": "No se encontró la empresa"}), response.status_code

    except requests.exceptions.RequestException as e:
        print(f"❌ Error en la consulta: {str(e)}")  # Imprime cualquier error en la consola
        return jsonify({"error": f"Error en la consulta: {str(e)}"}), 500

# Endpoint para obtener representantes legales de una empresa
@routes.route('/sunatData/verificarRepresentantesLegales', methods=['POST'])
def obtener_representate_legal():
    # Extraer el RUC del cuerpo de la solicitud
    req_data = request.get_json()
    if not req_data or "ruc" not in req_data:
        return jsonify({"error": "Se requiere el RUC"}), 400    

    ruc = req_data["ruc"]

    # Agregar el token en el cuerpo de la solicitud
    payload = {
        "token": API_TOKEN,  # Pasamos el token en el JSON
        "ruc": ruc
    }

    response = requests.post(API_URL_REPRESENTANTE_LEGAL, json=payload)

    if response.status_code == 200:
        data = response.json()
        representante = SunatRepresentanteLegalResponse(**data)
        return jsonify(representante.to_dict())
    else:
        return jsonify({"error": "No se encontró el representante legal"}), response.status_code   
    

@routes.route('/social/AgregarComentario', methods=['POST'])
def agregar_comentario():
        data = request.get_json()
        if not data or "usuario_id" not in data or "entidad_id" not in data or "entidad_tipo" not in data or "contenido" not in data:
            return jsonify({"error": "Datos incompletos"}), 400

        nuevo_comentario = agregar_comentario_bo(
            data["usuario_id"], data["entidad_id"], data["entidad_tipo"], data["contenido"]
        )
        
        return jsonify(nuevo_comentario), 201

@routes.route('/social/comentarios', methods=['POST'])
def obtener_comentarios():
    try:
        req_data = request.get_json()

        if not req_data or "entidad_id" not in req_data:
            return jsonify({"error": "Falta el parámetro entidad_id"}), 400
        
        entidad_id = req_data["entidad_id"]

        comentarios = obtener_comentarios_bo(entidad_id)
        
        return jsonify(comentarios), 200

    except Exception as e:
        return jsonify({"error": "Error al obtener comentarios", "detalle": str(e)}), 500

@routes.route('/social/comentarios/<comentario_id>', methods=['DELETE'])
def eliminar_comentario(comentario_id):
        resultado = eliminar_comentario_bo(comentario_id)
        return jsonify(resultado), 200

# endpoints para valorizaciones
@routes.route('/social/valorizacion', methods=['POST'])
def agregar_valorizacion():
    try:
        req_data = request.get_json()
        
        if not req_data:
            return jsonify({"error": "Solicitud inválida. Se requiere JSON válido"}), 400
        
        if not all(k in req_data for k in ["ruc", "id_usuario", "estrellas"]):
            return jsonify({"error": "Faltan parámetros obligatorios (ruc, id_usuario, estrellas)"}), 400
        
        response = agregar_valorizacion_bo(req_data["ruc"], req_data["id_usuario"], req_data["estrellas"])
        
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": "Error en la API", "detalle": str(e)}), 500

@routes.route('/social/valorizacion/promedio', methods=['POST'])
def obtener_promedio_valorizacion():
    """Endpoint para obtener el promedio de valoraciones de una empresa (POST en lugar de GET)."""
    req_data = request.get_json()

    if not req_data or "ruc" not in req_data:
        return jsonify({"error": "Falta el parámetro 'ruc'"}), 400
    
    resultado = obtener_promedio_valorizaciones_bo(req_data["ruc"])
    return jsonify(resultado), 200 if "error" not in resultado else 400