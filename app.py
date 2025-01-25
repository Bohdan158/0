from flask import Flask, request, jsonify
from database import init_db, get_orders, add_order

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def view_orders():
    return jsonify(get_orders())

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    if not data.get('address'):
        return jsonify({"error": "Address is required"}), 400
    return jsonify(add_order(data))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
