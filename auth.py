from flask import Blueprint, jsonify, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    if dados.get("usuario") == "admin" and dados.get("senha") == "123":
        return jsonify({"token": "token-ficticio"})
    return jsonify({"msg": "Credenciais inválidas"}), 401
