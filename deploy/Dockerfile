FROM nvcr.io/nvidia/morpheus/mlflow-triton-plugin:latest
WORKDIR /app
RUN apt-get update && apt-get install -y python3-pip
COPY . .
ENTRYPOINT ["python", "main.py"]