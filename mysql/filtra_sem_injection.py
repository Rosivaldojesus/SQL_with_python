from funcao_conecta_DB import nova_conexao

# Usando o LIKE
# Termina: (%letras)
# No meio: (%letras%)
# Que começa: (letras%)

comando_sql = 'SELECT * FROM contatos WHERE nome LIKE %s'

with nova_conexao() as conexao:
    nome = input('Nome a ser localizado: ')
    args = (f'%{nome}%',)

    cursor = conexao.cursor()
    cursor.execute(comando_sql, args)

    for x in cursor:
        print(x)
