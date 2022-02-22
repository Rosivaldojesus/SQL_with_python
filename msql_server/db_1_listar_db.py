from conectarDB import conectar_banco_dados

conexao = conectar_banco_dados()

cursor = conexao.cursor()
cursor.execute("SHOW DATABASES")

'''
for db in cursor:
    print(f'Database: {db[0]}')
'''
print("=============================================")

for i, db in enumerate(cursor, start=1):
    print(f'{i}: {db[0]}')