from conexoes import conectar_banco_dados
from mysql.connector import ProgrammingError

# Conectando ao Banco de Dados Mysql
conexao = conectar_banco_dados()

cursor = conexao.cursor()

try:
    cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')
except ProgrammingError as error:
    print(f'Erro conexão: {error.msg}')
