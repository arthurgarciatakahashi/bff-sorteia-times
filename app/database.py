# app/database.py
import psycopg2

DB_CONFIG = {
    'dbname': 'verceldb',
    'user': 'default',
    'password': 'uOUi0s6MeqoC',
    'host': 'ep-summer-morning-a4y75lf1-pooler.us-east-1.aws.neon.tech',
    'port': 5432
}

def obter_conexao():
    return psycopg2.connect(**DB_CONFIG)
