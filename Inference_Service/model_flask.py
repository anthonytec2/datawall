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
    print(parsed_data)'
    return "something"

def calculate_payout(requestor, percent_dict, base_cost):
    comp_part = []
    comp_dw = 0
    for participant in percent_dict:
        if participant == requestor:
            comp_part.append((participant, (.985 * base_cost * percent[participant] * (1-percent[requestor])**2) / (1-percent[requestor])))
            comp_dw += (.015 * base_cost * percent[participant] * (1-percent[requestor])**2) / (1-percent[requestor])
    cost = base_cost * (1 - percent_dict[requestor])**2
    return cost, comp_dw, comp_part

app.run(host = "0.0.0.0", port = 5000, debug = True)