from funcao_conecta_DB import nova_conexao
from mysql.connector.errors import ProgrammingError

tabela_contatos = """
    CREATE TABLE contatos(
        nome VARCHAR(10),
        tel VARCHAR(40)
    )
 """

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')

