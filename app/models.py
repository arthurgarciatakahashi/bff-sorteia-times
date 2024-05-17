# app/models.py
from pydantic import BaseModel

class JogadorBase(BaseModel):
    nome: str
    posicao: str
    nota: float
    ativo: bool

class Jogador(BaseModel):
    id: int
    nome: str = None
    posicao: str  = None
    nota: float = None
    ativo: bool = None

class JogadorCreate(BaseModel):
    nome: str
    posicao: str
    nota: float
    ativo: bool

class Config:
    orm_mode = True
