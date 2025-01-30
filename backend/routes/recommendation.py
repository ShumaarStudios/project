from flask import Blueprint, request, jsonify
from models.extracts import Extract
import random

recommendation_bp = Blueprint('recommendation', __name__)

@recommendation_bp.route('/suggest', methods=['POST'])
def suggest():
    data = request.json
    soil_type = data['soil_type']
    crop_variety = data['crop_variety']
    recommendations = Extract.query.filter_by(region=data['region']).all()
    response = [{"name": rec.name, "dosage": rec.dosage, "application_method": rec.application_method} for rec in recommendations]
    return jsonify(response), 200
