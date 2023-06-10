FROM python:3.8-slim
  
COPY . /workspace

WORKDIR /workspace

RUN pip install -r requirements.txt

ENTRYPOINT uvicorn app:app --host 0.0.0.0 --port 8000
