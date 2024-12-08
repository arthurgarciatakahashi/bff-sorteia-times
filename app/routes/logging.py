# app/routes/logging.py
from fastapi import APIRouter, HTTPException, Response
from ..procedures import criar_log, obter_todos_os_logs
from ..models import RegistroLog
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/logs")
def obter_todos_jogadores(response: Response):
    data = obter_todos_os_logs()

    logs = data['logs']
    total_count = data['total_count']
    # Cria a resposta JSON
    json_response = JSONResponse(content=logs)

    # Adiciona o cabeçalho com o total de registros
    json_response.headers["X-Total-Count"] = str(total_count)

    return json_response

@router.post("/logs")
def criar_novo_log(log: RegistroLog):
    return criar_log(log)
