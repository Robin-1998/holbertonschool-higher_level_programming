#!/usr/bin/env python3
""" API Security and Authentication Techniques """
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def route_proteger():
    return ("Basic Auth: Access Granted")

# la formet avec le suite de code est utilisé pour l'authentification
# notamment si tu utilises un module comme Flask-HTTPAuth

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')

    user = users.get(username)
    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_token), 200

@app.route('/jwt-protected', methods=['GET'])
@auth.login_required
def jwt_protected():
    return ("JWT Auth: Access Granted")


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

if __name__ == '__main__':
    app.run()
