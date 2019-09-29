# pip3 install psycopg2
# sudo apt-get build-dep python3-psycopg2
# pip install psycopg2
import psycopg2 as sys

conexao = psy.connect(
    database='nomedatabase',
    user='nomeuser',
    password='senha',
    host='localhost')


query = """select id,param1,param2,param3 from tabela where tabela = '1'"""
cursor = conexao.cursor()
cursor.execute(query)
rows = cursor.fetchall()

for r in rows:
    print(f'id {r[0]} param1 {r[1]} param1 {r[2]} param3 {r[3]}')
conexao.close()
