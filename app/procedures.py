# app/procedures.py
import psycopg2
from fastapi import HTTPException
from .database import obter_conexao
from .models import Jogador, JogadorBase, JogadorCreate
import json

def obter_todos_os_jogadores():
    conn = None
    try:
        conn = obter_conexao()
        cur = conn.cursor()
        cur.execute("SELECT public.get_all_jogadores_count()")

        # Recupera o resultado da função
        result = cur.fetchone()[0]

        # Adiciona log para ver o resultado bruto
        print("Resultado da função PostgreSQL:", result)

        # Fecha o cursor e a conexão
        cur.close()
        conn.close()

        # Result é uma string JSON, então usamos json.loads para convertê-lo em um dicionário Python
        data = result

        # Adiciona log para ver os dados convertidos
        print("Dados convertidos:", data)

        return data
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return {"jogadores": [], "total_count": 0}
    except Exception as e:
        print(f"Erro ao obter os dados dos jogadores: {e}")
        return {"jogadores": [], "total_count": 0}

def criar_jogador(jogador: JogadorCreate):
    try:
        connection = obter_conexao()
        cursor = connection.cursor()
        postgres_insert_query = """ 
            SELECT inserir_jogador(%s, %s, %s, %s);
        """
        record_to_insert = (jogador.nome, jogador.posicao, jogador.nota, jogador.ativo)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        return {"message": "Jogador criado com sucesso!"}
    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=500, detail=str(error))
    finally:
        if connection:
            cursor.close()
            connection.close()

import psycopg2
from fastapi import HTTPException
from .database import obter_conexao
from .models import Jogador

def obter_jogador_por_id(jogador_id: int) -> Jogador:
    try:
        connection = obter_conexao()
        cursor = connection.cursor()

        # Chamar a função usando a sintaxe de uma função no PostgreSQL
        cursor.execute("SELECT * FROM obter_jogador_por_id(%s)", (jogador_id,))

        # Recuperar os resultados
        jogador_data = cursor.fetchone()
        if jogador_data is None:
            raise HTTPException(status_code=404, detail="Jogador não encontrado")

        # Construir e retornar o objeto Jogador
        jogador = Jogador(
            id=jogador_data[0], 
            nome=jogador_data[1], 
            posicao=jogador_data[2], 
            nota=float(jogador_data[3]) if jogador_data[3] is not None else None, 
            ativo=jogador_data[4]
        )
        return jogador
    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=500, detail=str(error))
    finally:
        if connection:
            cursor.close()
            connection.close()


def atualizar_jogador(jogador_id: int, jogador: JogadorBase):
    try:
        connection = obter_conexao()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT atualizar_jogador(%s, %s, %s, %s, %s)
            """,
            (jogador_id, jogador.nome, jogador.posicao, jogador.nota, jogador.ativo)
        )
        connection.commit()
        return {"message": "Jogador atualizado com sucesso!"}
    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=500, detail=str(error))
    finally:
        if connection:
            cursor.close()
            connection.close()



def deletar_jogador(jogador_id: int):
    try:
        connection = obter_conexao()
        cursor = connection.cursor()
        cursor.execute("SELECT deletar_jogador(%s)", (jogador_id,))
        connection.commit()
        return {"message": "Jogador deletado com sucesso"}
    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=500, detail=str(error))
    finally:
        if connection:
            cursor.close()
            connection.close()


