from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from contextlib import contextmanager


paramentros_database = dict(
    host='localhost',
    port='3308',
    user='root',
    passwd='admin123',
    database='agenda'
)

@contextmanager
def nova_conexao():
    conexao = connect(**paramentros_database)
    try:
        yield conexao
    finally:
        if(conexao and conexao.is_connected()):
            conexao.close()