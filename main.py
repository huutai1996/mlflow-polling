import os

from config.init import get_config
import time
import mlflowtriton
if __name__ == '__main__':
    config = get_config()
    mlflow_triton_client = mlflowtriton.MlflowTriton()
    while True:
        model_alias = mlflow_triton_client.get_models_with_alias()
        model_triton = mlflowtriton.get_model_triton()
        for model_name, model_version in model_alias.items():
            if model_name in model_triton:
                if model_triton[model_name] != model_version:
                    mlflow_triton_client.update_deployment_triton(model_name, model_version)
            else:
                mlflow_triton_client.create_deployment_triton(model_name, model_version)
        time.sleep(int(config.INTERVAL))




