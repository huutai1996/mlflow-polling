FROM python:3.11.9
WORKDIR /app
COPY . .
RUN apt update && apt install -y python3-pip git
RUN pip install "importlib-metadata<=8.5.0,>=6.0" && pip install setuptools
RUN git clone https://github.com/triton-inference-server/server.git
RUN cd server/deploy/mlflow-triton-plugin && python setup.py install && cd /app && rm -rf server
CMD ["python3", "main.py"]