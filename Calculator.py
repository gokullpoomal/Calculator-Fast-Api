
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Gokul Calculator API")

# Home API
@app.get("/")
def home():
    return {"message": "Welcome to Calculator API"}

# Addition
@app.get("/add")
def addition(a: float, b: float):
    return {"operation": "Addition", "result": a + b}

# Subtraction
@app.get("/subtract")
def subtraction(a: float, b: float):
    return {"operation": "Subtraction", "result": a - b}

# Multiplication
@app.get("/multiply")
def multiplication(a: float, b: float):
    return {"operation": "Multiplication", "result": a * b}

# Division
@app.get("/divide")
def division(a: float, b: float):
    if b == 0:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero"
        )
    return {"operation": "Division", "result": a / b} 
