from funcao_conecta_DB import nova_conexao

comando_sql = 'SELECT * FROM contatos WHERE tel ="99653-4782" '

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(comando_sql)

    for x in cursor:
        print(x[1])