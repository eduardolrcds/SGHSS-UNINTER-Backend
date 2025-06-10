from flask import Blueprint, jsonify, request

pacientes_bp = Blueprint('pacientes', __name__)

PACIENTES = []

@pacientes_bp.route('/', methods=['GET'])
def listar():
    return jsonify(PACIENTES)

@pacientes_bp.route('/', methods=['POST'])
def criar():
    novo = request.get_json()
    PACIENTES.append(novo)
    return jsonify({"msg": "Paciente adicionado"}), 201
