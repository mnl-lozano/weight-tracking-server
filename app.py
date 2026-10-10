from traceback import print_tb

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/api/status")
def status():
    return jsonify({
        "status": "OK",
        "message": "Hello from Flask!"
    })
@app.post("/api/send-weight")
def receive_weight():
    weight_data = request.json

    print("Weight data received!")
    print(weight_data)

    return jsonify({
        "status": "OK",
        "message": "Weight received successfully"
    })

def update_database():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
