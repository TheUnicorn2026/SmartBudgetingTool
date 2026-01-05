from flask import Flask, request, jsonify, redirect, url_for

app = Flask(__name__)

# In-memory list to store users (acting as a database)
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "password": "abcd", "phone": "12345"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "password": "abcde", "phone": "123456"}
]

# Home route: Display all users
@app.route('/')
def index():
    return jsonify(users)

# Create user route: Add a new user
@app.route('/add', methods=["POST"])
def add_user():
    data = request.get_json()
    new_id = len(users) + 1  # Generate a new ID
    new_user = {"id": new_id, "name": data['name'], "email": data['email'], "password": data["password"], "phone": data["phone"]}
    users.append(new_user)
    return jsonify({"message": "User added successfully", "user": new_user}), 201

@app.route('/temp', methods=["POST"])
def temp():
    data = request.get_json()
    print(data)
    for i in range(5):
        print(i, "_", end=" ")
    return jsonify({"success": "true"}), 201

# Edit user route: Update an existing user
@app.route('/edit/<int:id>', methods=["PUT"])
def edit_user(id):
    user = next((user for user in users if user["id"] == id), None)
    
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify({"message": "User updated successfully", "user": user})

# Delete user route
@app.route('/delete/<int:id>', methods=["DELETE"])
def delete_user(id):
    global users
    user = next((user for user in users if user["id"] == id), None)
    
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    users = [u for u in users if u["id"] != id]
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
