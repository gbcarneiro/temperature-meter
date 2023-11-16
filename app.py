from flask import Flask, request 
from datetime import datetime

app = Flask(__name__)

@app.route('/add/temperature', methods=['POST'])
def add_temperature(): 
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        timestamp = datetime.now()
        return str(timestamp)
    