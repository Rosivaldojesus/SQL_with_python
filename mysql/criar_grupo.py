from conexoes import conectar_banco_dados


criar_tabela_grupo= """
    CREATE TABLE IF NOT EXISTS grupos (id INT AUTO_INCREMENT PRIMARY KEY, descricao VARCHAR(40))
"""

alterar_tabela_contato_1 = """
    ALTER TABLE contatos ADD grupo_id INT
"""

alterar_tabela_contato = """
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES grupos_id
"""

conexao = conectar_banco_dados()

cursor = conexao.cursor()
#cursor.execute(criar_tabela_grupo)
#cursor.execute(alterar_tabela_contato)
cursor.execute(alterar_tabela_contato_1)

