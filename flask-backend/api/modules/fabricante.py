import functools
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.manufacturer import (
    get_fabricante,
    get_manufacturer,
    create_manufacturer,
    get_manufacturer_by_name,
    update_manufacturer,
    delete_manufacturer,
)

bp = Blueprint('fabricante', __name__, url_prefix='/fabricante')
CORS(bp)

@bp.route('/', methods=['GET'])
def list():
    retorno = get_fabricante()
    return jsonify(retorno)

@bp.route('/<int:manufacturer_id>', methods=['GET'])
def get(manufacturer_id):
    return jsonify(get_manufacturer(manufacturer_id))

@bp.route('/by_name/<manufacturer_name>', methods=['GET'])
def get_by_name(manufacturer_name):
    return jsonify(get_manufacturer_by_name(manufacturer_name))

@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    Nombre_Empresa = data['Nombre_Empresa']
    Contacto = data['Contacto']
    Direccion = data['Direccion']
    Email = data['Email']
    Calificacion = data['Calificacion']
    return jsonify(create_manufacturer(Nombre_Empresa, Contacto, Direccion, Email, Calificacion))

@bp.route('/<int:manufacturer_id>', methods=['PUT'])
def update(manufacturer_id):
    data = request.get_json()
    nombre_empresa = data['Nombre_Empresa']
    contacto = data['Contacto']
    direccion = data['Direccion']
    email = data['Email']
    calificacion = data['Calificacion']
    return jsonify(update_manufacturer(nombre_empresa, contacto, direccion, email, calificacion, manufacturer_id))

@bp.route('/<int:manufacturer_id>', methods=['DELETE'])
def delete(manufacturer_id):
    return jsonify(delete_manufacturer(manufacturer_id))