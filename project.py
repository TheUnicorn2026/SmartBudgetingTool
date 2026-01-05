from flask import Flask, request, jsonify, abort

app = Flask(__name__)

<<<<<<< HEAD
# Users in-memory storage
users = []
user_id_counter = 1

@app.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    global user_id_counter
    if not request.json or 'User_name' not in request.json or 'Email' not in request.json:
        abort(400, description="User_name and Email are required")

    user = {
        'User_id': user_id_counter,
        'User_name': request.json['User_name'],
        'Email': request.json['Email'],
        'Phone': request.json.get('Phone', ""),
        'Password': request.json.get('Password', ""),
        'Type': request.json.get('Type', ""),
        'Created_by': request.json.get('Created_by', None),
        'Updated_by': request.json.get('Updated_by', None)
    }
    users.append(user)
    user_id_counter += 1
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID"""
    user = next((u for u in users if u['User_id'] == user_id), None)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user"""
    user = next((u for u in users if u['User_id'] == user_id), None)
    if user is None:
        abort(404, description="User not found")

    if not request.json:
        abort(400, description="Invalid request body")

    user['User_name'] = request.json.get('User_name', user['User_name'])
    user['Email'] = request.json.get('Email', user['Email'])
    user['Phone'] = request.json.get('Phone', user['Phone'])
    user['Password'] = request.json.get('Password', user['Password'])
    user['Type'] = request.json.get('Type', user['Type'])
    user['Created_by'] = request.json.get('Created_by', user['Created_by'])
    user['Updated_by'] = request.json.get('Updated_by', user['Updated_by'])

    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user"""
    global users
    user = next((u for u in users if u['User_id'] == user_id), None)
    if user is None:
        abort(404, description="User not found")

    users = [u for u in users if u['User_id'] != user_id]
=======
# In-memory storage
todos = ["sakshi"]
id_counter = 1

@app.route('/todos', methods=['GET'])
def get_todos():
    """Get all todos"""
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    """Create a new todo"""
    global id_counter
    if not request.json or 'title' not in request.json:
        abort(400, description="Title is required")
    
    todo = {
        'id': id_counter,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'completed': request.json.get('completed', False)
    }
    todos.append(todo)
    id_counter += 1
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a specific todo by ID"""
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo is None:
        abort(404, description="Todo not found")
    return jsonify(todo)

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update an existing todo"""
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo is None:
        abort(404, description="Todo not found")
    
    if not request.json:
        abort(400, description="Invalid request body")
        
    todo['title'] = request.json.get('title', todo['title'])
    todo['description'] = request.json.get('description', todo['description'])
    todo['completed'] = request.json.get('completed', todo['completed'])
    
    return jsonify(todo)

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    global todos
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if todo is None:
        abort(404, description="Todo not found")
    
    todos = [item for item in todos if item['id'] != todo_id]
>>>>>>> c66b35f (initial comment)
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)