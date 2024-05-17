# app/main.py
from fastapi import FastAPI
from .routes.jogadores import router as jogadores_router

app = FastAPI()

app.include_router(jogadores_router, prefix="/jogadores", tags=["jogadores"])

@app.get("/")
def read_root():
    return {"message": "Running!"}


