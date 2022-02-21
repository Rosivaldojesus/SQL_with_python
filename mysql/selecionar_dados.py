from conexoes import conectar_banco_dados

conexao = conectar_banco_dados()

sql = 'SELECT * FROM contatos'

cursor = conexao.cursor()
cursor.execute(sql)

contatos = cursor.fetchall()

print(contatos)


for contato in contatos:
    print(f'{contato[2]} - {contato[0]} {contato[1]}' )
