import numpy as np
import json
import onnx
from caffe2.python.onnx import backend

# Load ONNX model
graph = onnx.load("dataWall.onnx")

# Load model into Caffe2
model = backend.prepare(graph, device="CPU")