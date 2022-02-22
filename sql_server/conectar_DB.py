import pyodbc
conexao = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-HVTNLUB\SQLEXPRESS;"
    "Database=agenda;"
    "Trusted_Connection=yes;"
    )

cursor = conexao.cursor()

cursor.execute('SELECT * FROM cidade')


for row in cursor:
    print('row = %r' % (row,))

