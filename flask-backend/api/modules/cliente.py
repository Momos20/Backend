import functools
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.client import (
    get_cliente,
    get_client,
    create_client,
    get_client_by_name,
    update_client,
    delete_client,
)

bp = Blueprint('cliente', __name__, url_prefix='/cliente')
CORS(bp)

@bp.route('/', methods=['GET'])
def list():
    retorno = get_cliente()
    return jsonify(retorno)

@bp.route('/<int:client_id>', methods=['GET'])
def get(client_id):
    return jsonify(get_client(client_id))

@bp.route('/by_name/<client_name>', methods=['GET'])
def get_by_name(client_name):
    return jsonify(get_client_by_name(client_name))

@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    name = data['name']
    Contact = data['Contact']
    Direccion = data['Direccion']
    Email= data['Email']
    return jsonify(create_client(name, Contact, Direccion, Email))

@bp.route('/<int:client_id>', methods=['PUT'])
def update(client_id):
    data = request.get_json()
    name = data['name']
    Contact = data['Contact']
    Direccion = data['Direccion']
    Email= data['Email']
    return jsonify(update_client(name, Contact, Direccion, Email, client_id))

@bp.route('/<int:client_id>', methods=['DELETE'])
def delete(client_id):
    return jsonify(delete_client(client_id))