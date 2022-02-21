from conexoes import conectar_banco_dados

# A variável conexao receber a função conectar_banco_dados()
conexao = conectar_banco_dados()


cursor = conexao.cursor()
cursor.execute("SHOW TABLES")

for i, table in enumerate(cursor, start=1):
    print(f'Tabela {i}: {table[0]}')

