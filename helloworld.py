import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def Hello():
    return ("Hello world")
