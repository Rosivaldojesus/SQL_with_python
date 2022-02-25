from funcao_conecta_DB import nova_conexao

comando_sql = 'SELECT * FROM contatos ORDER BY nome DESC'

with nova_conexao() as conexao:

    cursor = conexao.cursor()
    cursor.execute(comando_sql)

    print('\n'.join(str(registro) for registro in cursor))
