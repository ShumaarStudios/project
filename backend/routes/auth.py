from flask import Blueprint, request, jsonify
from models.user import User, db
import random

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(name=data['name'], email=data.get('email'), mobile_number=data['mobile_number'], password=data['password'], role='farmer')
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(mobile_number=data['mobile_number'], password=data['password']).first()
    if user:
        return jsonify({"message": "Login successful", "user_id": user.id}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/otp', methods=['POST'])
def generate_otp():
    mobile_number = request.json['mobile_number']
    otp = random.randint(100000, 999999)
    # Send OTP via SMS service (not implemented)
    return jsonify({"otp": otp}), 200
