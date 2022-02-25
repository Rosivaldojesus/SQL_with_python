from funcao_conecta_DB import nova_conexao
from mysql.connector.errors import ProgrammingError

comando_sql = 'DELETE FROM contatos WHERE nome = %s'
args = ('Ana',)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(comando_sql, args)
        conexao.commit()

    except FloatingPointError as error:
        print(f'Erro: {error.msg}')

    else:
        print(f'{cursor.rowcount} Registro excluído com sucesso')
