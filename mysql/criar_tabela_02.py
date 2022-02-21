from conexoes import conectar_banco_dados

# Variável com conecta ao DB
conexao = conectar_banco_dados()

mycursor = conexao.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS cidade (nome VARCHAR(50))")

