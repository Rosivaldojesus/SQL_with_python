from conexoes import conectar_banco_dados
from mysql.connector.errors import ProgrammingError

conexao = conectar_banco_dados()

cursor = conexao.cursor()
#comando_sql = 'SELECT tel, nome FROM contatos'
comando_sql = 'SELECT tel, nome FROM contatos LIMIT 3 OFFSET 10'
cursor.execute(comando_sql)

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())