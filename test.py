import json

# String representation of a list of dictionaries
string = '[{"name": "onnx-test-triton-plugin", "version": "1", "state": "READY", "triton_model_path": "/triton_models/onnx-test-triton-plugin", "mlflow_model_uri": "models:/onnx-test-triton-plugin/2", "flavor": "onnx"}]'

# Convert string to list of dictionaries
list_of_dicts = json.loads(string)

dict_temp = {}
for i in list_of_dicts:
    model_name = i['name']
    model_uri  = i['mlflow_model_uri']
    model_version = model_uri.split('/')[-1]
    dict_temp[model_name] = model_version
print(dict_temp)
