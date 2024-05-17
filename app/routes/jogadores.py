# app/routes/jogadores.py
from fastapi import APIRouter, HTTPException
from ..procedures import criar_jogador, obter_jogador_por_id, atualizar_jogador, deletar_jogador, obter_todos_os_jogadores
from ..models import JogadorCreate

router = APIRouter()


@router.get("/jogadores")
def obter_todos_jogadores():
    jogadores = obter_todos_os_jogadores()
    if not jogadores:
        raise HTTPException(status_code=404, detail="Não há jogadores cadastrados")
    return jogadores

@router.post("/jogadores")
def criar_novo_jogador(jogador: JogadorCreate):
    return criar_jogador(jogador)

@router.get("/jogadores/{jogador_id}")
def obter_jogador(jogador_id: int):
    return obter_jogador_por_id(jogador_id)

@router.put("/jogadores/{jogador_id}")
def atualizar_jogador_endpoint(jogador_id: int, jogador: JogadorCreate):
    return atualizar_jogador(jogador_id, jogador)

@router.delete("/jogadores/{jogador_id}")
def deletar_jogador_endpoint(jogador_id: int):
    return deletar_jogador(jogador_id)

