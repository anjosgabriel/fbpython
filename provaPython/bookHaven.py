import pymysql
import os
import time
from classeUsuario import Usuario
from Livraria import Produtolivraria

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def incluir(cursor, id_produtolivraria, quantidade):
    cursor.execute('SELECT * FROM produtolivraria WHERE id_produtolivraria = %s', (id_produtolivraria,))
    resultado = cursor.fetchone()
    if resultado:
        produto = Produtolivraria(*resultado)
        try:
            produto.atualizar_estoque(quantidade, 'entrada')
            cursor.execute('UPDATE produtolivraria SET estoque = %s WHERE id_produtolivraria = %s',
                           (produto.estoque, produto.id_produtolivraria))
            print("Estoque atualizado com sucesso!")
        except ValueError as e:
            print(e)
    else:
        print("Produto não encontrado!")

def retirar(cursor, id_produtolivraria, quantidade):
    cursor.execute('SELECT * FROM produtolivraria WHERE id_produtolivraria = %s', (id_produtolivraria,))
    resultado = cursor.fetchone()
    if resultado:
        produto = Produtolivraria(*resultado)
        try:
            produto.atualizar_estoque(quantidade, 'saida')
            cursor.execute('UPDATE produtolivraria SET estoque = %s WHERE id_produtolivraria = %s',
                           (produto.estoque, produto.id_produtolivraria))
            print("Estoque atualizado com sucesso!")
        except ValueError as e:
            print(e)
    else:
        print("Produto não encontrado!")

def cadastrar_usuario(cursor):
    print("-" * 20)
    print("CADASTRAMENTO DE USUÁRIO")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cursor.execute('INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)', (nome, email, senha))
    con.commit()
    print("Usuário cadastrado com sucesso!")
    time.sleep(2)

def alterar_usuario(cursor):
    print("-" * 20)
    print("ALTERAÇÃO DE USUÁRIO")
    id_usuario = int(input("ID do usuário: "))
    nome = input("Novo Nome: ")
    email = input("Novo Email: ")
    senha = input("Nova Senha: ")
    cursor.execute('UPDATE usuario SET nome=%s, email=%s, senha=%s WHERE id_usuario=%s', (nome, email, senha, id_usuario))
    con.commit()
    print("Usuário alterado com sucesso!")
    time.sleep(2)

def listar_usuarios(cursor):
    print("-" * 20)
    print("LISTAGEM DE USUÁRIOS")
    cursor.execute('SELECT * FROM usuario')
    resultados = cursor.fetchall()
    for linha in resultados:
        print(f'ID: {linha[0]}, Nome: {linha[1]}, Email: {linha[2]}')
    input("Pressione Enter para continuar...")

def excluir_usuario(cursor):
    print("-" * 20)
    print("EXCLUSÃO DE USUÁRIO")
    id_usuario = int(input("ID do usuário a ser excluído: "))
    cursor.execute('DELETE FROM usuario WHERE id_usuario=%s', (id_usuario,))
    con.commit()
    print("Usuário excluído com sucesso!")
    time.sleep(2)

def verificar_usuario(cursor, id_usuario):
    cursor.execute('SELECT * FROM usuario WHERE id_usuario = %s', (id_usuario,))
    return cursor.fetchone()

def imprimir_saida(cliente, produtos):
    print("-" * 20)
    print("NOTA FISCAL")
    print(f"Cliente: {cliente[1]}")
    print(f"Email: {cliente[2]}")
    print("Produtos Comprados:")
    for produto in produtos:
        print(f"Descrição: {produto['descricao']}, Quantidade: {produto['quantidade']}, Valor: {produto['valor']}")
    print("-" * 20)

def realizar_compra(cursor):
    print("-" * 20)
    print("REALIZAR COMPRA")
    id_usuario = int(input("ID do usuário: "))
    cliente = verificar_usuario(cursor, id_usuario)
    if not cliente:
        print("Usuário não encontrado!")
        time.sleep(2)
        return
    
    carrinho = []
    while True:
        id_produtolivraria = int(input("ID do produto (0 para finalizar): "))
        if id_produtolivraria == 0:
            break
        quantidade = int(input("Quantidade: "))
        cursor.execute('SELECT * FROM produtolivraria WHERE id_produtolivraria = %s', (id_produtolivraria,))
        produto = cursor.fetchone()
        if produto:
            carrinho.append({
                'id': produto[0],
                'descricao': produto[1],
                'editora': produto[2],
                'valor': produto[3],
                'quantidade': quantidade
            })
        else:
            print("Produto não encontrado!")

    total = sum(item['valor'] * item['quantidade'] for item in carrinho)
    print(f"Total da compra: R$ {total:.2f}")
    confirmar = input("Deseja confirmar a compra? (s/n): ").strip().lower()
    if confirmar == 's':
        for item in carrinho:
            retirar(cursor, item['id'], item['quantidade'])
        con.commit()
        imprimir_saida(cliente, carrinho)
        print("Compra realizada com sucesso!")
    else:
        print("Compra cancelada!")

limpaTela()
# Criar o banco de dados
con = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='bookhaven'
)

with con:
    with con.cursor() as cursor:
        # Criar tabela usuario
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                senha VARCHAR(100) NOT NULL
            )
        ''')

        # Criar tabela produtolivraria
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtolivraria (
                id_produtolivraria INT AUTO_INCREMENT PRIMARY KEY,
                descricao VARCHAR(200) NOT NULL,
                editora VARCHAR(50) NOT NULL,
                valor DOUBLE(10,2),
                estoque INT NOT NULL
            )
        ''')
        con.commit()

    # Programa principal - CRUD
    with con.cursor() as cursor:
        while True:
            limpaTela()
            print("1 - Cadastrar Usuário")
            print("2 - Alterar Usuário")
            print("3 - Listar Usuários")
            print("4 - Excluir Usuário")
            print("-" * 20)
            print("5 - Cadastrar Produto")
            print("6 - Alterar Produto")
            print("7 - Listar Produtos")
            print("8 - Excluir Produto")
            print("9 - Movimento de Estoque")
            print("10 - Realizar Compra")
            print("11 - Sair")
            op = input("Escolha o numero da sua opção: ")

            if op == '11':
                time.sleep(2)
                print("Até breve...")
                break

            elif op == '1':
                cadastrar_usuario(cursor)

            elif op == '2':
                alterar_usuario(cursor)

            elif op == '3':
                listar_usuarios(cursor)

            elif op == '4':
                excluir_usuario(cursor)

                #tabela produtolivraria
            
            elif op == '5':
                print("-" * 20)
                print("CADASTRAMENTO DE PRODUTO")
                descricao = input("Descrição: ")
                editora = input("Editora: ")
                valor = float(input("Valor: "))
                estoque = int(input("Estoque: "))
                if estoque > 18 or estoque <= 0:
                    print("Estoque inválido. Deve ser um valor positivo menor ou igual a 18.")
                else:
                    cursor.execute('''
                        INSERT INTO produtolivraria (descricao, editora, valor, estoque)
                        VALUES (%s, %s, %s, %s)
                    ''', (descricao, editora, valor, estoque))
                    con.commit()
                    print("Produto cadastrado com sucesso!")
                time.sleep(2)

            elif op == '6':
                print("-" * 20)
                print("ALTERAÇÃO DE PRODUTO")
                id_produtolivraria = int(input("ID do produto: "))
                descricao = input("Nova Descrição: ")
                editora = input("Nova Editora: ")
                valor = float(input("Novo Valor: "))
                estoque = int(input("Novo Estoque: "))
                if estoque > 18 or estoque <= 0:
                    print("Estoque inválido. Deve ser um valor positivo menor ou igual a 18.")
                else:
                    cursor.execute('''
                        UPDATE produtolivraria
                        SET descricao=%s, editora=%s, valor=%s, estoque=%s
                        WHERE id_produtolivraria=%s
                    ''', (descricao, editora, valor, estoque, id_produtolivraria))
                    con.commit()
                    print("Produto alterado com sucesso!")
                time.sleep(2)

            elif op == '7':
                print("-" * 20)
                print("LISTAGEM DE PRODUTOS")
                cursor.execute('SELECT * FROM produtolivraria')
                resultados = cursor.fetchall()
                for linha in resultados:
                    print(f'ID: {linha[0]}, Descrição: {linha[1]}, Editora: {linha[2]}, Valor: {linha[3]}, Estoque: {linha[4]}')
                input("Pressione Enter para continuar...")

            elif op == '8':
                print("-" * 20)
                print("EXCLUSÃO DE PRODUTO")
                id_produtolivraria = int(input("ID do produto a ser excluído: "))
                cursor.execute('DELETE FROM produtolivraria WHERE id_produtolivraria=%s', (id_produtolivraria,))
                con.commit()
                print("Produto excluído com sucesso!")
                time.sleep(2)

            elif op == '9':
                print("-" * 20)
                print("MOVIMENTO DE ESTOQUE")
                id_produtolivraria = int(input("ID do produto: "))
                tipo_movimento = input("Tipo de movimento (entrada/saida): ").strip().lower()
                quantidade = int(input("Quantidade: "))

                if tipo_movimento == 'entrada':
                    incluir(cursor, id_produtolivraria, quantidade)
                elif tipo_movimento == 'saida':
                    retirar(cursor, id_produtolivraria, quantidade)
                else:
                    print("Tipo de movimento inválido!")

                con.commit()
                time.sleep(2)

            elif op == '10':
                realizar_compra(cursor)

        