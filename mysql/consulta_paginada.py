from mysql.connector.errors import ProgrammingError
from funcao_conecta_DB import nova_conexao

#sql = 'SELECT * FROM contatos'
sql = 'SELECT * FROM contatos LIMIT %s OFFSET %s'
argumentos = (3, 7)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, argumentos)
        contatos = cursor.fetchall()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        for contato in  contatos:
            print(f'{contato[2]:2d} -{contato[0]:15s} Telefone: {contato[1]}')