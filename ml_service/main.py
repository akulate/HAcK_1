from fastapi import FastAPI
from triage_predict import triage_predict
from drug_verify import verify_drug

app = FastAPI()

@app.post("/triage/predict")
def triage(data: dict):
    return triage_predict(data["symptoms"], data["age"])

@app.post("/drug/verify")
def drug(data: dict):
    return verify_drug(data)
