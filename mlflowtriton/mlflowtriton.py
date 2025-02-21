import json
import subprocess
import sys

import mlflow
from config.init import get_config
from logger.logger import get_logger
import logging
import  ast


def get_model_triton() -> dict:
    command = ["mlflow", "deployments", "list",  "-t",  "triton"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError("Error in getting Triton models")
    models_triton = ast.literal_eval(result.stdout.splitlines()[1])
    model_dict = {}
    for i in models_triton:
        model_name = i['name']
        model_uri  = i['mlflow_model_uri']
        model_version = model_uri.split('/')[-1]
        model_dict[model_name] = model_version
    return model_dict


class MlflowTriton:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.config = get_config()
        self.uri = self.config.MLFLOW_URI
        if not self.uri:
            self.logger.log(logging.ERROR, "MLFLOW_URI is not set")
            sys.exit(1)
        self.alias = self.config.ALIAS
        if not self.alias:
            self.logger.log(logging.ERROR, "ALIAS is not set")
            sys.exit(1)
        self.client = mlflow.tracking.MlflowClient(tracking_uri=self.uri)
    def get_models_with_alias(self) -> dict:
        models = self.client.search_registered_models()
        models_alias = {}
        for model in models:
            if self.alias in model.aliases:
                models_alias[model.name] = model.aliases[self.alias]
                self.logger.log(logging.INFO, f"Model {model.name} with alias {self.alias} found")
        return models_alias

    def create_deployment_triton(self, model_name, version):
        command = ["mlflow", "deployments", "create", "-t",  "triton", "--flavor", "onnx", "-m",  f"models:/{model_name}/{version}",  "--name", model_name]
        create_result = subprocess.run(command, capture_output=True, text=True)
        if create_result.returncode != 0:
            self.logger.log(logging.ERROR, f"Error in creating Triton deployment for model {model_name}: {create_result.stderr}")
        else:
            self.logger.log(logging.INFO, f"Model {model_name} with version {version} deployed successfully")
    def update_deployment_triton(self, model_name, version):
        command = ["mlflow", "deployments", "update", "-t",  "triton", "--flavor", "onnx", "-m",  f"models:/{model_name}/{version}",  "--name", model_name]
        update_result = subprocess.run(command, capture_output=True, text=True)
        if update_result.returncode != 0:
            print(update_result.stderr)
            self.logger.log(logging.ERROR, f"Error in updating Triton deployment for model {model_name}: {update_result.stdout}")
        else:
            self.logger.log(logging.INFO, f"Model {model_name} with version {version} updated successfully")






