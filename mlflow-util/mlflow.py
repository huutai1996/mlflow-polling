import mlflow
from config import get_config
class Mlflow:
    def __init__(self):
        self.config = get_config()
        self.uri = self.config.MLFLOW_URI
        self.s3_access_key = self.config.MLFLOW_S3_ACCESS_KEY
        self.s3_secret_key = self.config.MLFLOW_S3_SECRET_KEY
        self.alias = self.config.alias
        self.client = mlflow.tracking.MlflowClient(tracking_uri=self.uri)
    def get_models_with_alias(self, alias):
        models = mlflow.search_registered_model()
        models_alias = {}
        for model in models:
            if alias in model.aliases:
                models_alias[model.name] = model.aliases[alias]
        return models_alias



