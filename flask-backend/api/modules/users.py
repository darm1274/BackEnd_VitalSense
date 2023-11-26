from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.users import (
    get_users, get_user, create_user, update_user, delete_user,
    get_patients, get_patient, create_patient, update_patient, delete_patient,
)

bp = Blueprint('users', __name__, url_prefix='/users')
CORS(bp)

# Usuarios
@bp.route('/users', methods=['GET'])
def list_users():
    return jsonify(get_users())

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    return jsonify(get_user(user_id))

@bp.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    print(data)
    return jsonify(create_user(data))

@bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json()
    return jsonify(update_user(user_id, data))

@bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    return jsonify(delete_user(user_id))

# Pacientes
@bp.route('/patients', methods=['GET'])
def list_patients():
    return jsonify(get_patients())

@bp.route('/patients/<int:pat_id>', methods=['GET'])
def get_patient_route(pat_id):
    return jsonify(get_patient(pat_id))

@bp.route('/patients', methods=['POST'])
def create_patient_route():
    data = request.get_json()
    return jsonify(create_patient(data))

@bp.route('/patients/<int:pat_id>', methods=['PUT'])
def update_patient_route(pat_id):
    data = request.get_json()
    return jsonify(update_patient(pat_id, data))

@bp.route('/patients/<int:pat_id>', methods=['DELETE'])
def delete_patient_route(pat_id):
    return jsonify(delete_patient(pat_id))
