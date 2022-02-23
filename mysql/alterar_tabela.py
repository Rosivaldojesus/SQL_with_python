from conexoes import conectar_banco_dados
from mysql.connector import ProgrammingError

alterar_tabela = 'ALTER TABLE contatos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'

try:
    conexao = conectar_banco_dados()
    cursor = conexao.cursor()
    cursor.execute(alterar_tabela)
except ProgrammingError as error:
    print(f'Erro: {error.msg}')

