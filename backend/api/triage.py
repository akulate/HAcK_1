from fastapi import APIRouter
from services.ml_client import call_triage

router = APIRouter()

@router.post("/submit")
def submit(data: dict):
    result = call_triage(data["symptoms"], data["age"])
    return {
        "name": data["name"],
        "urgency": result["label"],
        "reason": result["reason"]
    }
