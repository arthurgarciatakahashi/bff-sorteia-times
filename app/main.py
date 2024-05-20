# app/main.py
from fastapi import FastAPI
# from .routes.jogadores import router as jogadores_router

from .routes import jogadores
import os
app = FastAPI()

# app.include_router(jogadores_router, prefix="/jogadores", tags=["jogadores"])
app.include_router(jogadores.router)

@app.get("/")
def read_root():
    return {"message": "Running!"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)