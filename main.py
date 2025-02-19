from config.init import get_config
import mlflowtriton
if __name__ == '__main__':
    config = get_config()
    print(config)
    mlflow_triton_client = mlflowtriton.MlflowTriton()
    model_alias = mlflow_triton_client.get_models_with_alias()
    print (model_alias)



