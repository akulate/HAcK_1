import requests

ML_URL = "http://localhost:8001"

def call_triage(symptoms, age):
    r = requests.post(f"{ML_URL}/triage/predict",
                      json={"symptoms": symptoms, "age": age})
    return r.json()
