import pymysql

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',  
    password = 'allisom1',
    database = 'db'
)
try:
    with conexao.cursor() as cursor:
        # Executa uma consulta SQL simples
        cursor.execute("SELECT VERSION()")
        versao = cursor.fetchone()
        print(f"Versão do MySQL: {versao[0]}")
finally:
    conexao.close()
