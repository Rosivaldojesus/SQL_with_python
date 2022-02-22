from conectarDB import conectar_banco_dados

conexao = conectar_banco_dados()

cursor = conexao.cursor()
cursor.execute("SHOW TABLES")

for i, table in enumerate(cursor):
    print(f'Tabela {i}: {table[0]}')

