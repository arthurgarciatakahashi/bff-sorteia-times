# app/routes/jogadores.py
from fastapi import APIRouter, HTTPException, Response
from ..procedures import criar_jogador, obter_jogador_por_id, atualizar_jogador, deletar_jogador, obter_todos_os_jogadores
from ..models import JogadorCreate
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/jogadores")
def obter_todos_jogadores(response: Response):
    data = obter_todos_os_jogadores()

    players = data['jogadores']
    total_count = data['total_count']

    # Cria a resposta JSON
    json_response = JSONResponse(content=players)
    
    # Adiciona o cabeçalho com o total de registros
    json_response.headers["X-Total-Count"] = str(total_count)

    return json_response

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

