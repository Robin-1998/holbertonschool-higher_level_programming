#!/usr/bin/env python3
""" API Security and Authentication Techniques """
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)


app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

payload = {
    'username': 'user1',
    'password': 'password'
}

#hashing password
hashed_pw = generate_password_hash("mdp")
print(hashed_pw)

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None

@app.route('/login', methods=['POST'])
def login():


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def route_proteger():
    return("Basic Auth: Access Granted".format(auth.current_user))
# la formet avec le suite de code est utilisé pour l'authentification
# notamment si tu utilises un module comme Flask-HTTPAuth

@app.route('jwt-protected', methods=['GET'])
@auth.login_required
def jwt_protected():
    return ("JWT Auth: Access Granted")

@app.route('/admin-only', methods=['GET'])
def admin():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

if __name__=='__main__':
    app.run()
