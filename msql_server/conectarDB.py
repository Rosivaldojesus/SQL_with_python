from mysql.connector import connect

#  A função connect() do módulo mysel.connect aceita vários parâmetos nomeados, os mais importantes são:
#  host, port, user e password

def conectar_banco_dados():
    conexao = connect(host='localhost', port='3308', user='root', passwd='admin123', database='banco')
    return conexao

'''
try:
    conectar_banco_dados()
    print("Conectado ao Banco de Dados")
except:
    print('Ops! Ocorrreu um erro com a conexao')

'''
