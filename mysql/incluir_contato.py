from mysql.connector.errors import ProgrammingError
from funcao_conecta_DB import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Rosivaldo', '99653-4782')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        print('1 registro incluído, ID', cursor.lastrowid)