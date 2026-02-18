#!/usr/bin/python3
"""Develop a Simple API using Python with Flask"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Return the list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return the status"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return full user object if exists"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the API"""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added successfully",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
