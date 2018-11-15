import numpy as np
import json
import onnx
import torch
from caffe2.python.onnx import backend

# Load ONNX model
graph = onnx.load("dataWall.onnx")

# Load model into Caffe2
model = backend.prepare(graph, device="CPU")

dummy_input = np.random.rand(1,9).astype(np.float32)

output = model.run(dummy_input)

print(output)
