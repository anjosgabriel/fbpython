import pymysql
import os

def limpatela():
    os.system('cls')

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='agenda'
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")

resultados = cursor.fetchall()

print(resultados)

#inserindo dados 

dados = ("Maria Aparecida", "ma@gmail.com", "11 98888-8888", "Exemplo de inserção em python")

cursor.execute("INSERT INTO usuarios (nome, email, telefone, mensagem) values(%s,%s,%s,%s)",dados)

conexao.commit()

cursor.execute("SELECT * FROM usuarios")

resultados = cursor.fetchall()

print(resultados)




#fechamento da conexao 
conexao.close()