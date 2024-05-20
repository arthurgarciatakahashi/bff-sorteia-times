# app/main.py
from fastapi import FastAPI
from .routes import jogadores
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(jogadores.router)

# Configurar origens permitidas
origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://seu-dominio-front-end.com",
    "https://bff-sorteia-times.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir essas origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc)
    allow_headers=["*"],  # Permitir todos os headers
)

@app.get("/")
def read_root():
    return {"message": "Running!"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)