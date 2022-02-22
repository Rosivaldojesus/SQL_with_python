from funcao_conecta_DB import nova_conexao
from mysql.connector.errors import ProgrammingError

tabela_emails = """
    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_emails)
            print(f'Tabela criada com sucesso!')
        except ProgrammingError as error:
            print(f'Erro: {error.msg}')
except ProgrammingError as error:
    print(f'Erro Externo: {error.msg}')