from fastapi import APIRouter

router = APIRouter()

@router.post("/verify")
def verify(data: dict):
    # call ML here
    return {
        "status": "AUTHENTIC",
        "confidence": 0.92
    }
