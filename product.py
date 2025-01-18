from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
import json
from config import *
from bson import ObjectId, json_util
from config import *

# Initialize the Blueprint for product routes
product_bp = Blueprint('product', __name__)

# List Product Function
@product_bp.route('/products/list')
def productList():
    try:
        # Test the connection
        data = db.products.find() # products - Collection name
        data_list = list(data)

        json_data = json.dumps(data_list, default=json_util.default)
        return jsonify(json.loads(json_data)), 200  # Status code 200

    except Exception as e:
        return f"Error: {e}"
    
# Save Product Function
@product_bp.route('/products/add', methods=['POST'])
def save_product():

    data = request.get_json()

    # Map the incoming JSON data to product fields
    product = {
        'name': data.get('name'),
        'category': data.get('category'),
        'delete_status': data.get('delete_status', False),
        'description': data.get('description'),
        'sku': data.get('sku'),
        'status': data.get('status', True),
        'stock': data.get('stock', 0),
        'sub_category': data.get('sub_category'),
        'url': data.get('url'),
        'actual_cost': data.get('actual_cost'),
        'selling_cost': data.get('selling_cost')
    }

    # Insert the product into the database
    try:
        product_id = db.products.insert_one(product).inserted_id
        print(f'Inserted product ID: {product_id}')
        return jsonify({"message": "Product saved successfully!", "id": str(product_id)}), 201
    except Exception as e:
        print(f"Error inserting product: {e}")
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Product saved successfully!", "id": str("product_id")}), 201


# Edit Product Function
@product_bp.route('/products/edit/<product_id>', methods=['PUT'])
def edit_product(product_id):
    data = request.get_json()
    print(product_id)
    # Find the product by its ID
    product = db.products.find_one({"_id": ObjectId(product_id)})

    if not product:
        return jsonify({"message": "Product not found"}), 404
    
    updated_product = {}
    if 'name' in data:
        updated_product['name'] = data['name']
    if 'category' in data:
        updated_product['category'] = data['category']
    if 'description' in data:
        updated_product['description'] = data['description']
    if 'sku' in data:
        updated_product['sku'] = data['sku']
    if 'status' in data:
        updated_product['status'] = data['status']
    if 'stock' in data:
        updated_product['stock'] = data['stock']
    if 'sub_category' in data:
        updated_product['sub_category'] = data['sub_category']
    if 'url' in data:
        updated_product['url'] = data['url']
    if 'actual_cost' in data:
        updated_product['actual_cost'] = data['actual_cost']
    if 'selling_cost' in data:
        updated_product['selling_cost'] = data['selling_cost']

    # Update the product in the database
    db.products.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": updated_product}
    )

    return jsonify({"message": "Product updated successfully!"})
