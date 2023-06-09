from fastapi import FastAPI
from pydantic import BaseModel


class Box1(BaseModel):
    Name: str
    code_no: int
    quantity: int
    Pieces: int
    Brand_name: str

    app = FastAPI
    results = []

    @app.post("/container1")
    def create_storage(self: str, results: int):
        results.append(Box1)
        return {"Results": results}

    @app.get("/solution")
    def total_price(self=str, results: int):
        return {"Results": results}
