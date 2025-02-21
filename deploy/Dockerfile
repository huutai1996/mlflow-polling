FROM nvcr.io/nvidia/morpheus/mlflow-triton-plugin:latest
WORKDIR /app
RUN apt-get update && apt-get install -y python3-pip
COPY . .
CMD ["python3", "app.py"]