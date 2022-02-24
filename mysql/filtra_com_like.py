from funcao_conecta_DB import nova_conexao

# Usando o LIKE
# Termina: (%letras)
# No meio: (%letras%)
# Que começa: (letras%)

comando_sql = 'SELECT * FROM contatos WHERE nome LIKE "%v%" '

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(comando_sql)

    for x in cursor:
        print(x)
