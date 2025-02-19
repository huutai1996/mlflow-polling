import os
class Config:
    def __init__(self):
        self.MLFLOW_URI = os.getenv('MLFLOW_URI')
        self.MLFLOW_S3_ACCESS_KEY = os.getenv('MLFLOW_S3_ACCESS_KEY')
        self.MLFLOW_S3_SECRET_KEY = os.getenv('MLFLOW_S3_SECRET_KEY')
        self.ALIAS = os.getenv('ALIAS')
        self.TRITON_URI = os.getenv('TRITON_URI')
_config = None
def get_config():
    global _config
    if _config is None:
        _config = Config()
    return _config