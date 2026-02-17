"""
get,post,delete users from route
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users=[]

@app.get("/users")
def get_users():
    return jsonify(users)

@app.post("/users")
def add_user():
    data=request.json
    users.append(data)
    return {"status":"created"},201

@app.delete("/users/<int:i>")
def delete_user(i):
    users.pop(i)
    return {"status":"deleted"}

app.run()