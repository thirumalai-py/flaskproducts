# app.py
from flask import Flask, request, jsonify
import json
from bson import json_util
from config import *
from product import product_bp

# Load the Flask
app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return "Hello, Flask!"

# Register the product blueprint
app.register_blueprint(product_bp)

if __name__ == "__main__":
    app.run(debug=True)
