import pymysql

try:
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='fbradesco',
        database='bank'
    )

    cursor = conexao.cursor()
except:
    print("Problemas de conexão")