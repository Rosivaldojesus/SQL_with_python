from conexoes import conectar_banco_dados


tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos (nome VARCHAR(50), tel (VARCHAR(40)
    )
"""

conexao = conectar_banco_dados()

cursor = conexao.cursor()
cursor.execute(tabela_contatos)

