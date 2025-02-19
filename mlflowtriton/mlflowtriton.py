import sys

import mlflow
from config.init import get_config
from logger.logger import get_logger
import logging
class MlflowTriton:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.config = get_config()
        self.uri = self.config.MLFLOW_URI
        if not self.uri:
            self.logger.log(logging.ERROR, "MLFLOW_URI is not set")
            sys.exit(1)
        self.s3_access_key = self.config.MLFLOW_S3_ACCESS_KEY
        self.s3_secret_key = self.config.MLFLOW_S3_SECRET_KEY
        self.alias = self.config.ALIAS
        if not self.alias:
            self.logger.log(logging.ERROR, "ALIAS is not set")
            sys.exit(1)
        self.client = mlflow.tracking.MlflowClient(tracking_uri=self.uri)
        self.triton_uri = self.config.TRITON_URI

    def get_models_with_alias(self) -> dict:
        models = self.client.search_registered_models()
        models_alias = {}
        for model in models:
            if self.alias in model.aliases:
                models_alias[model.name] = model.aliases[self.alias]
                self.logger.log(logging.INFO, f"Model {model.name} with alias {self.alias} found")
        return models_alias
    def check_model_exist_triton(self, model_name) -> (bool, str):
        pass






