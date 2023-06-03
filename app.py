from fastapi import FastAPI
from hello import sum_xy

from data_models import SamplePostRequest

app = FastAPI()

@app.get("/")
def home():
    return "Another hello"

@app.get("/sum/{c}")
def sum_xy_endpoint(c:str, a: int, b: int):
    return c + " " + str(sum_xy(a, b))

@app.post("/predict")
def predict(request: SamplePostRequest):

    return [request.a + request.c[0]]

@app.get("/predict")
def predict():
    return "From predict function get"

@app.get("/health")
def health_check():
    return "OK"
