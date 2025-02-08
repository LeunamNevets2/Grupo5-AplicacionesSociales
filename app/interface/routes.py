from flask import Blueprint, request, jsonify
from business.usuario_bo import crear_usuario
from business.empresa_bo import crear_empresa

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