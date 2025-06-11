#!/usr/bin/env python3
""" Develop a simple API unsing Python with Flask """
from flask import Flask, jsonify, request

# on créé une instance flask
app = Flask(__name__)

users = {}


# define a route and a view function
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# define a route with data


@app.route('/data')
def data_user():
    usernames = list(users.keys())
    return jsonify(usernames)

# define a route with status


@app.route('/status')
def data_status():
    return "OK"

# define a route with status


@app.route('/users/<string:username>')
def data_username(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# define a route avec ajout d'un nouvel utilisateur


@app.route('/add_user', methods=['GET', 'POST'])
def adding_users():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
