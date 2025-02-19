from config.init import get_config

if __name__ == '__main__':
    config = get_config()
    print(config.MLFLOW_URI)
    print(config.MLFLOW_S3_ACCESS_KEY)
    print(config.MLFLOW_S3_SECRET_KEY)
