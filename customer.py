from flask import Flask, request, jsonify
app = Flask(__name__)

customers = []

#POST METHOD

@app.route('/addcustomer',methods=['POST'])
def add_customer():
    
    data = request.json

    customer={
        "id": len(customers) + 1,
        "name":data['name'],
        "email":data['email'],
        "password":data['password'],
        "address":data['address']
    }

    customers.append(customer)
    return jsonify({"message": "customer added successfully","customer": customer})

@app.route('/getallcustomer', methods=['GET'])
def get_all_customers():
    return jsonify(customers)


@app.route('/updatecustomer/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data=request.json

    for customer in customers:
        if customer['id'] == customer_id:
            customer['name'] = data.get('name',customer['name'])
            customer['email'] = data.get('email',customer['email'])
            customer['password'] = data.get('password',customer['password'])
            return jsonify({"message": "customer updated","customer": customer})
            return jsonify({"message": "customer not found"})
            

@app.route('/deletecustomer/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    for customer in customers:
        if customer['id'] == customer_id:
            customers.remove(customer)
            return jsonify({"message": "customer deleted","customer": customer})
            return jsonify({"message": "customer not found"})



print("end reached")
print(app.url_map)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
