from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt_claims
from functools import wraps
# from models import Users
from werkzeug.security import generate_password_hash, check_password_hash

# Mock user database
users = {
    'user1': {'password': generate_password_hash('password1'), 'role': 'passenger'},
    'user2': {'password': generate_password_hash('password2'), 'role': 'business manager'},
    'user3': {'password': generate_password_hash('password3'), 'role': 'Intasend admin'}
}

def auth_routes(app, db):
    # User login endpoint
    @app.route('/login', methods=['POST'])
    def login():
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            user = users.get(username)
            if not user or not check_password_hash(user['password'], password):
                return jsonify({'message': 'Invalid username or password'}), 401
            # Generate JWT token with user's role as a claim
            access_token = create_access_token(identity=username, additional_claims={'role': user['role']})
            return jsonify({'access_token': access_token, 'role': user['role']}), 200
        except Exception as e:
            return jsonify({'message': 'An error occurred while processing your request'}), 500

    # Protected routes by role
    def role_required(required_role):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                claims = get_jwt_claims()
                if claims['role'] != required_role:
                    return jsonify({'message': 'Insufficient permissions'}), 403
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @app.route('/passenger/dashboard')
    @jwt_required()
    @role_required('passenger')
    def passenger_dashboard():
        # Serve passenger dashboard data
        current_user = get_jwt_identity()
        return jsonify({'message': f'Passenger dashboard data for {current_user}'}), 200

    @app.route('/manager/dashboard')
    @jwt_required()
    @role_required('business manager')
    def manager_dashboard():
        # Serve manager dashboard data
        current_user = get_jwt_identity()
        return jsonify({'message': f'Manager dashboard data for {current_user}'}), 200

    @app.route('/admin/dashboard')
    @jwt_required()
    @role_required('Intasend admin')
    def admin_dashboard():
        # Serve admin dashboard data
        current_user = get_jwt_identity()
        return jsonify({'message': f'Admin dashboard data for {current_user}'}), 200