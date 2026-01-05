from flask import Flask, request, jsonify
app = Flask(__name__)

users = []

#POST METHOD

@app.route('/adduser',methods=['POST'])
def add_user():
    
    data = request.json

    user={
        "id": len(users) + 1,
        "name":data['name'],
        "email":data['email'],
        "password":data['password'],
        "phone":data['phone']
    }

    users.append(user)
    return jsonify({"message": "user added successfully","user": user})

@app.route('/getdata', methods=['GET'])
def get_all_users():
    return jsonify(users)


@app.route('/updateuser/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data=request.json

    for user in users:
        if user['id'] == user_id:
            user['name'] = data.get('name',user['name'])
            user['email'] = data.get('email',user['email'])
            user['password'] = data.get('password',user['password'])
            user['phone'] = data.get('phone',user['phone'])
            return jsonify({"message": "user updated","user": user})
            return jsonify({"message": "user not found"})

@app.route('/deleteuser/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({"message": "user deleted","user": user})
            return jsonify({"message": "user not found"})



print("end reached")
print(app.url_map)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
