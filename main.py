from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sample FastAPI app!"}

@app.get("/hello/")
def say_hello(name: Optional[str] = Query(None, description="Name to greet")):
    if name:
        return {"message": f"Hello, {name}!"}
    return {"message": "Hello, World!"}

@app.get("/sum/")
def sum_numbers(a: int = Query(..., description="First number"), b: int = Query(..., description="Second number")):
    return {"sum": a + b} 