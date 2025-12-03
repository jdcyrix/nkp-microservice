from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SumRequest(BaseModel):
    a: float
    b: float

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/sum")
def sum_numbers(body: SumRequest):
    return {"result": body.a + body.b}
