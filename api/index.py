import json
from flask import Flask, request, jsonify
import base64
import boto3
app = Flask(__name__)
client = boto3.client('rekognition')

@app.route('/')
def ping():
    return jsonify({'message': 'pong!'})

@app.route('/tarea3-201020831', methods=['POST'])
def rekognition():
    req = json.loads(request.data)
    res = client.detect_labels(
        Image= {
            'Bytes': base64.b64decode(req['image'])
        },
        MaxLabels=10
    )

    return jsonify(res)

app.run(debug=True)