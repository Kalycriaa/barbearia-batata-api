from database import db
from barbearia_batata.services import barbearia_services
from flask import Blueprint, jsonify, request

barbearia_bp = Blueprint("barbearia_batata", __name__)

@barbearia_bp.route("/barbearia_batata", methods = ['GET'])
def listar_clientes():
    resposta = barbearia_services.listar_clientes()
    if not resposta:
        return jsonify({"error": "nenhum registro localizado, adicione no minimo 1 registro"}), 404
    
    return jsonify(resposta), 200

@barbearia_bp.route("/barbearia_batata/<int:id>", methods = ['GET'])
def listar_clientes_id(id):
    resposta = barbearia_services.listar_clientes_id(id)
    if not resposta:
        return jsonify({"error": "nenhum registro localizado"}), 404
    
    return jsonify(resposta), 200

@barbearia_bp.route("/barbearia_batata", methods = ['POST'])
def incluir_clientes():
    dados = request.get_json()
    if not dados or "nome" not in dados or "horario" not in dados or "data" not in dados:
        return jsonify({"error": "por favor preencher todos campos obrigatorios"}), 400
    
    resposta = barbearia_services.incluir_cliente(dados)
    
    return jsonify(resposta), 200

@barbearia_bp.route("/barbearia_batata/<int:id>", methods = ['PUT'])
def atualizar_clientes_id(id):
    dados = request.get_json()
    if not dados:
        return jsonify({"error": "por favor preencher no minimo 1 campo"}), 400
    
    resposta = barbearia_services.atualizar_cliente(id, dados)
    if not resposta:
        return jsonify({"error": "registro nao localizado"}), 404
    
    return jsonify(resposta), 200

@barbearia_bp.route("/barbearia_batata/<int:id>", methods = ['DELETE'])
def deletar_cliente(id):
    resposta = barbearia_services.deletar_cliente(id)
    if not resposta:
        return jsonify({"error": "registro nao localizado"}), 404
    
    return jsonify(resposta), 200


