FROM google/cloud-sdk:411.0.0-slim

WORKDIR /app

COPY . /app

RUN apt update -y && apt-get update && \
    pip3 install --upgrade pip && \
    apt-get install python3 -y && pip3 install -r requirements.txt && \
    pip3 install torch torchvision  --extra-index-url https://download.pytorch.org/whl/cu116 

CMD ["python3", "app.py"]