from conectarDB import conectar_banco_dados

conexao = conectar_banco_dados()


cursor = conexao.cursor()
cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()

#print(clientes)

for cliente in clientes:
    print(f'{cliente[0]} - {cliente[1]}- {cliente[2]}- {cliente[3]}- {cliente[4]}- {cliente[5]}- {cliente[6]}')
