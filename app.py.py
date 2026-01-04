from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Test route
@app.route('/')
def home():
    return "Hello, your Python backend is working!"

# Route to handle order
@app.route('/place-order', methods=['POST'])
def place_order():
    data = request.get_json()
    print("Order received:", data)
    return jsonify({"message": "Order received!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)