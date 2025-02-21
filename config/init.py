import os
class Config:
    def __init__(self):
        self.MLFLOW_URI = os.getenv('MLFLOW_URI', 'http://10.110.69.25:5000')
        self.ALIAS = os.getenv('ALIAS', 'testing')
        self.INTERVAL = os.getenv('INTERVAL', '300')
_config = None
def get_config():
    global _config
    if _config is None:
        _config = Config()
    return _config