from traceback import print_tb

from flask import Flask, jsonify, request
from flask_cors import CORS
from database import ConnectToDB, CreateDB, LogWeightInDataBase
import os.path

app = Flask(__name__)
CORS(app)

dataBaseFileName = "weight_tracker.db"

if os.path.isfile(dataBaseFileName):
    print("Database file found.")
    cursor = ConnectToDB(dataBaseFileName) # This is not necessary
else:
    print("Database file missing. Creating new one.")#
    cursor = CreateDB(dataBaseFileName)


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

    LogWeightInDataBase(dataBaseFileName, weight_data)

    return jsonify({
        "status": "OK",
        "message": "Weight received successfully"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
