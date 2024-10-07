#print("Hello world")

import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def Hello():
    return ("Hello world")

# Run Uvicorn server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)