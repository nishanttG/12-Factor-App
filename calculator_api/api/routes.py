from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Operation(BaseModel):
    a: float
    b: float

@router.get("/")
def read_root():
    return {"message": "Welcome to the Calculator API"}

@router.post("/add")
def add(data: Operation):
    return {"result": data.a + data.b}

@router.post("/subtract")
def subtract(data: Operation):
    return {"result": data.a - data.b}

@router.post("/multiply")
def multiply(data: Operation):
    return {"result": data.a * data.b}

@router.post("/divide")
def divide(data: Operation):
    if data.b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": data.a / data.b}
