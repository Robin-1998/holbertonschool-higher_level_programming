#!/usr/bin/env python3
""" Develop a simple API unsing Python with Flask """
from flask import Flask, jsonify, request

# on créé une instance flask
app = Flask(__name__)

users = {
    "jane": {
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


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


@app.route('/add_user', methods=['POST'])
def adding_users():
    data = request.get_json()

    required = ["username", "name", "age", "city"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    username = data["username"]

    users[username] = {
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    return jsonify({"message": "User added", "user": {username: users[username]}}), 201


if __name__ == "__main__":
    app.run()
