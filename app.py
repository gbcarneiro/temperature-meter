from flask import Flask, jsonify, request 
from datetime import datetime
from pymongo.mongo_client import MongoClient

app = Flask(__name__)

mongo_uri = f"mongodb+srv://gabrielcarneiro:{password}@cluster0.qfs6xtz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)

db = client["teste"]
collection = db["temperature"]

@app.route('/add/temperature', methods=['POST'])
def add_temperature(): 
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        timestamp = datetime.now()

        data = {
            "temperatura": json['temperature'],
            "timestamp": str(timestamp)
        }
        result = collection.insert_one(data)
        return jsonify({"success": True, "message": "Document inserted successfully", "id": str(result.inserted_id)})
    