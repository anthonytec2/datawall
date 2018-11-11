import onnx

model = onnx.load("dataWall.onnx")

onnx.checker.check_model(model)