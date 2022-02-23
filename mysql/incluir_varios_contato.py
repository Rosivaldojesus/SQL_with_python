from mysql.connector.errors import ProgrammingError
from funcao_conecta_DB import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Rosivaldo', '99653-4782'),
    ('Paula', '99653-4782'),
    ('Leticia', '99653-4782'),
    ('João', '99653-4782'),
    ('Ana', '99653-4782'),
    ('Joana', '99653-4782'),
    ('Maria', '99653-4782'),
    ('Pedro', '99653-4782'),
    ('Fernanda', '99653-4782'),
    ('Caroline', '99653-4782'),
    ('Patrica', '99653-4782'),
    ('Flavia', '99653-4782'),

)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as error:
        print(f'Erro: {error.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros')