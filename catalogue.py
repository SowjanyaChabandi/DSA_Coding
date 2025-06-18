from flask import jsonify
from flask import Flask, request
from flask_cors import CORS
from flask_restx import Namespace

app = Flask(__name__)
CORS(app)

apartments = [
    {"id": 1, "city": "Hyderabad", "rent": 15000},

    {"id": 2, "city": "Mumbai", "rent": 16000},
]

new_id = 3

itemns = Namespace("catalogue", description="", path="/items")

def init_routes(api):
    api.add_namespace(itemns)


@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(apartments)

@app.route('/api/items', methods=['POST'])
def create_items():
    global new_id
    data = request.get_json()
    new_item = {
        "id": new_id,
        "city": data['city'],
        "rent": int(data['rent'])
    }
    apartments.append(new_item)
    new_id += 1
    return jsonify(new_item), 201


@app.route('/api/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    for item in apartments:
        if item['id'] == id:
            item['city'] = data['city']
            item['rent'] = data['rent']
            return jsonify(item)
    
    return jsonify({"error": "Apartment not found"}), 404


@app.route('/api/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    apartments = [item for item in apartments if item['id'] != id]
    return jsonify({"message": "Item deleted"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)