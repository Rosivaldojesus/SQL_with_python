from conexoes import conectar_banco_dados

conexao = conectar_banco_dados()
mycursor = conexao.cursor()


mycursor.execute("SHOW DATABASES")

# Percorrendo a lista do banco de dados
for x in mycursor:
    print(f'DB: {x[0]}')
