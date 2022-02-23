from mysql.connector.errors import ProgrammingError
from funcao_conecta_DB import nova_conexao

sql = 'SELECT tel, nome FROM contatos'
#sql = 'SELECT * FROM contatos LIMIT 5 OFFSET 5'

with nova_conexao() as conexao:

    cursor = conexao.cursor()
    cursor.execute(sql)

    for contato in cursor.fetchall():
        print('\t'.join(str(campo) for campo in contato))