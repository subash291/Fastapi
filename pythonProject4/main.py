from fastapi import FastAPI
import uvicorn
from services.inventory_service import storage_router

app_main = FastAPI()
app_main.include_router(storage_router)

if __name__ == "__main__":
    uvicorn.run("main:app_main")
