from funcao_conecta_DB import nova_conexao
from mysql.connector import ProgrammingError

excluir_tabela = 'DROP TABLE emails'

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(excluir_tabela)
            print('Tabela exluir com sucesso!!!')
        except ProgrammingError as error:
            print(f'Erro: {error.msf}')
except:
    print("OPS! Algo deu errado.")