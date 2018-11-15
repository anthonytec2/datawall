from flask import Flask, request
import numpy as np
import json
import onnx
import torch
from caffe2.python.onnx import backend

# Load ONNX model
graph = onnx.load("dataWall.onnx")

# Load model into Caffe2
model = backend.prepare(graph, device="CPU")

app = Flask(__name__)
@app.route('/', methods = ["GET"])
def home():
    return "you are at the homepage"

@app.route('/', methods = ["POST"])
def runmodel():
    parsed_data = request.data
    parsed_data = parsed_data.decode('utf-8')
    parsed_list = []
    parsed_data = parsed_data.split(',')
    print(parsed_data)
    return 'something'

app.run(host = "0.0.0.0", port = 5000, debug = True)
