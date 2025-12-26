from fastapi import FastAPI
from api import triage, drug

app = FastAPI(title="MedTech Backend")

app.include_router(triage.router, prefix="/api/triage")
app.include_router(drug.router, prefix="/api/drug")
