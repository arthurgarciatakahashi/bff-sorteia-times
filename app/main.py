# app/main.py
from fastapi import FastAPI
from .routes import jogadores

app = FastAPI()

app.include_router(jogadores.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)


# Configurações de conexão com o banco de dados

# SELECT proname
# FROM pg_catalog.pg_proc
# WHERE prokind = 'p'; 

# CREATE TABLE jogadores (
#     id SERIAL PRIMARY KEY,
#     nome VARCHAR(100) NOT NULL,
#     posição VARCHAR(50) NOT NULL,
#     nota DECIMAL(3, 2),
#     ativo BOOLEAN NOT NULL
# );

    
#     CREATE OR REPLACE FUNCTION get_all_jogadores()
# RETURNS JSON AS $$
# BEGIN
#     RETURN (
#         SELECT json_agg(row_to_json(jogadores))
#         FROM jogadores
#     );
# END;
# $$ LANGUAGE plpgsql;

# CREATE OR REPLACE PROCEDURE obter_jogador_por_id(
#     IN jogador_id INT,
#     OUT jogador_nome VARCHAR(100),
#     OUT jogador_posicao VARCHAR(50),
#     OUT jogador_nota DECIMAL(3, 2),
#     OUT jogador_ativo BOOLEAN
# )
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     SELECT nome, posição, nota, ativo
#     INTO jogador_nome, jogador_posicao, jogador_nota, jogador_ativo
#     FROM jogadores
#     WHERE id = jogador_id;
# END $$;
# CREATE OR REPLACE PROCEDURE deletar_jogador(
#     IN jogador_id INT
# )
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     DELETE FROM jogadores WHERE id = jogador_id;
# END $$;

# CREATE OR REPLACE PROCEDURE atualizar_jogador(
#     IN jogador_id INT,
#     IN novo_nome VARCHAR(100),
#     IN nova_posicao VARCHAR(50),
#     IN nova_nota DECIMAL(3, 2),
#     IN novo_ativo BOOLEAN
# )
# LANGUAGE plpgsql
# AS $$
# BEGIN
#     UPDATE jogadores
#     SET nome = novo_nome,
#         posição = nova_posicao,
#         nota = nova_nota,
#         ativo = novo_ativo
#     WHERE id = jogador_id;
# END $$;

