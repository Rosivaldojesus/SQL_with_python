import pyodbc

# Conectando ao banco de dados
conexao = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=DESKTOP-HVTNLUB\SQLEXPRESS;" 
                         "Database=agenda;" "Trusted_Connection=yes;")

mycursor = conexao.cursor()
mycursor.execute('SELECT * FROM cidade')

for linha in mycursor:
    print(f'{linha}')

