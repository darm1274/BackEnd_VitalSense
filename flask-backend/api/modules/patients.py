import functools
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from model.patients import (
    get_patients, get_patient, create_patient, update_patient, delete_patient,
)

bp = Blueprint('patients', __name__, url_prefix='/patients')
CORS(bp)

# patients routes
@bp.route('/patients', methods=['GET'])
def list_patients():
    return jsonify(get_patients())

@bp.route('/patients/<int:PAT_ID>', methods=['GET'])
def get_patients_route(PAT_ID):
    return jsonify(get_patient(PAT_ID))

@bp.route('/patients', methods=['POST'])
def create_patient_route():
    data = request.get_json()
    return jsonify(create_patient(data))

# @bp.route('/patients/<int:pat_id>', methods=['PUT'])
# def update_patient(pat_id):
#     data = request.get_json()
#     return jsonify(update_user(pat_id, data))

@bp.route('/patients/<int:PAT_ID>', methods=['DELETE'])
def delete_patient_route(PAT_ID):
    return jsonify(delete_patient(PAT_ID))

# # Patients routes
# @bp.route('/patients', methods=['GET'])
# def list_patients():
#     return jsonify(get_patient())

@bp.route('/patients/<int:pat_id>', methods=['GET'])
def get_patient_route(pat_id):
    return jsonify(get_patient(pat_id))

# @bp.route('/patients', methods=['POST'])
# def create_patient_route():
#     data = request.get_json()
#     return jsonify(create_patient(data))

@bp.route('/patients/<int:pat_id>', methods=['PUT'])
def update_patient_route(pat_id):
    data = request.get_json()
    return jsonify(update_patient(pat_id, data))

# @bp.route('/patients/<int:pat_id>', methods=['DELETE'])
# def delete_patient_route(pat_id):
#     return jsonify(delete_patient(pat_id))
