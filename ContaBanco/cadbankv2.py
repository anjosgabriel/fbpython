import pymysql
import os
import time

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='Banco'
   )

os.system("cls")

with conexao:
    with conexao.cursor() as cursor:
        TABLE_NAME = 'Poupanca'
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'numero INT NOT NULL,'
            'cpf VARCHAR(20) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL,'
            'ativa bool ,'
            'diaAniversarioPoupanca INT NOT NULL'
            ')'
        )
    conexao.commit()
    with conexao.cursor() as cursor:
        TABLE_NAME = 'Corrente'
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'numero INT NOT NULL,'
            'cpf VARCHAR(11) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL,'
            'ativa bool ,'
            'contadorTalao INT NOT NULL'
            ')'
        )
    conexao.commit()
    with conexao.cursor() as cursor:
        TABLE_NAME = 'Especial'
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'numero INT NOT NULL,'
            'cpf VARCHAR(11) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL,'
            'ativa bool ,'
            'limite double(10,2) NOT NULL'
            ')'
        )
    conexao.commit()    

    while True:
        os.system("cls")
        print('-'*80)
        print("Banco")
        print('-'*80)
        print("1 - Poupança")
        print("2 - Corrente")
        print("3 - Especial")
        print("4 - Sair")
        opcao_menu_principal=input("Digite sua opção :")
        if opcao_menu_principal=='4':
            break
        elif opcao_menu_principal=='1':
            while True:
                os.system("cls")
                print('-'*80)
                print("Banco - CONTA POUPANÇA")
                print('-'*80)
                print("1 - Cadastrar")
                print("2 - Alterar")
                print("3 - Apagar")
                print("4 - Movimentar")
                print("5 - Sair")
                sub_opcao_menu=input("Digite sua opção :")
                
                if sub_opcao_menu == '5':
                    break
                if sub_opcao_menu =='1':
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "poupanca"
                        numero = int(input("Digite o numero da conta : "))
                        cpf = input("Digita o cpf do cliente da conta :")
                        dia_aniversario_conta = int(input("Digite o dia de aniversario da conta : "))
                        dados = (numero, cpf, 0.00, 1, dia_aniversario_conta)
                        sql = f'INSERT INTO {TABLE_NAME} (numero, cpf, saldo, ativa, diaAniversarioPoupanca) VALUES (%s,%s,%s,%s,%s)'
                        cursor.execute(sql,dados)
                        conexao.commit()

                        sql =f'SELECT * FROM {TABLE_NAME}'
                        cursor.execute(sql)
                        resposta = cursor.fetchall()
                        print("Dados cadastrados")                    
                        for linha in resposta:
                            print(linha)
                    conexao.commit()
                    time.sleep(3)

                elif sub_opcao_menu == '2':  
                    numero_conta = int(input("Digite o número da conta que deseja alterar: "))
                    novo_cpf = input("Digite o novo CPF: ")
                    novo_dia_aniversario = int(input("Digite o novo dia de aniversário da conta: "))
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "poupanca"
                        sql = f'UPDATE {TABLE_NAME} SET cpf=%s, diaAniversarioPoupanca=%s WHERE numero=%s'
                        cursor.execute(sql, (novo_cpf, novo_dia_aniversario, numero_conta))
                    conexao.commit()
                    print("Conta atualizada com sucesso!")
                    time.sleep(3)

                elif sub_opcao_menu == '3':  
                    numero_conta = int(input("Digite o número da conta que deseja apagar: "))
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "poupanca"
                        sql = f'DELETE FROM {TABLE_NAME} WHERE numero=%s'
                        cursor.execute(sql, (numero_conta,))
                    conexao.commit()
                    print("Conta apagada com sucesso!")
                    time.sleep(3)


                elif sub_opcao_menu == '4':  
                    print("1 - Depositar")
                    print("2 - Sacar")
                    movimento = input("Digite sua opção: ")
                    numero_conta = int(input("Digite o número da conta: "))
                    valor = float(input("Digite o valor: "))
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "poupanca"  
                        if movimento == '1':  
                            sql = f'UPDATE {TABLE_NAME} SET saldo=saldo+%s WHERE numero=%s'
                        elif movimento == '2':  
                            sql = f'UPDATE {TABLE_NAME} SET saldo=saldo-%s WHERE numero=%s AND saldo >= %s'
                    cursor.execute(sql, (valor, numero_conta, valor))
                    if cursor.rowcount == 0:
                        print("Saldo insuficiente!")
                    else:
                        print("Transação concluída com sucesso!")
                    conexao.commit()
                    time.sleep(3)

                elif sub_opcao_menu == '5': 
                    sair = True
                    break 

        elif opcao_menu_principal=='2':
            while True:
                os.system("cls")
                print('-'*80)
                print("Banco - CONTA CORRENTE")
                print('-'*80)
                print("1 - Cadastrar")
                print("2 - Alterar")
                print("3 - Apagar")
                print("4 - Movimentar")
                print("5 - Sair")
                sub_opcao_menu=input("Digite sua opção :")
                
                if sub_opcao_menu == '5':
                    break
                if sub_opcao_menu =='1':
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "Corrente"
                        numero = int(input("Digite o numero da conta : "))
                        cpf = input("Digita o cpf do cliente da conta :")
                        dia_aniversario_conta = int(input("Digite o dia de aniversario da conta : "))
                        dados = (numero, cpf, 0.00, 1, dia_aniversario_conta)
                        sql = f'INSERT INTO {TABLE_NAME} (numero, cpf, saldo, ativa, diaAniversarioCorrente) VALUES (%s,%s,%s,%s,%s)'
                        cursor.execute(sql,dados)
                        conexao.commit()

                        sql =f'SELECT * FROM {TABLE_NAME}'
                        cursor.execute(sql)
                        resposta = cursor.fetchall()
                        print("Dados cadastrados")                    
                        for linha in resposta:
                            print(linha)
                    conexao.commit()
                    time.sleep(3)

                elif sub_opcao_menu == '2':  
                    numero_conta = int(input("Digite o número da conta que deseja alterar: "))
                    novo_cpf = input("Digite o novo CPF: ")
                    novo_dia_aniversario = int(input("Digite o novo dia de aniversário da conta: "))
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "Corrente"
                        sql = f'UPDATE {TABLE_NAME} SET cpf=%s, diaAniversarioPoupanca=%s WHERE numero=%s'
                        cursor.execute(sql, (novo_cpf, novo_dia_aniversario, numero_conta))
                    conexao.commit()
                    print("Conta atualizada com sucesso!")
                    time.sleep(3)

                elif sub_opcao_menu == '3':  
                    numero_conta = int(input("Digite o número da conta que deseja apagar: "))
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "Corrente"
                        sql = f'DELETE FROM {TABLE_NAME} WHERE numero=%s'
                        cursor.execute(sql, (numero_conta,))
                    conexao.commit()
                    print("Conta apagada com sucesso!")
                    time.sleep(3)


                elif sub_opcao_menu == '4':  
                    print("1 - Depositar")
                    print("2 - Sacar")
                    movimento = input("Digite sua opção: ")
                    numero_conta = int(input("Digite o número da conta: "))
                    valor = float(input("Digite o valor: "))
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "Corrente"  
                        if movimento == '1':  
                            sql = f'UPDATE {TABLE_NAME} SET saldo=saldo+%s WHERE numero=%s'
                        elif movimento == '2':  
                            sql = f'UPDATE {TABLE_NAME} SET saldo=saldo-%s WHERE numero=%s AND saldo >= %s'
                    cursor.execute(sql, (valor, numero_conta, valor))
                    if cursor.rowcount == 0:
                        print("Saldo insuficiente!")
                    else:
                        print("Transação concluída com sucesso!")
                    conexao.commit()
                    time.sleep(3)

                elif sub_opcao_menu == '5': 
                    sair = True
                    break 

        elif opcao_menu_principal=='3':
            while True:
                os.system("cls")
                print('-'*80)
                print("Banco - CONTA ESPECIAL")
                print('-'*80)
                print("1 - Cadastrar")
                print("2 - Alterar")
                print("3 - Apagar")
                print("4 - Movimentar")
                print("5 - Sair")
                sub_opcao_menu=input("Digite sua opção :")

                if sub_opcao_menu == '5':
                    break
                if sub_opcao_menu =='1':
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "Especial"
                        numero = int(input("Digite o numero da conta : "))
                        cpf = input("Digita o cpf do cliente da conta :")
                        dia_aniversario_conta = int(input("Digite o dia de aniversario da conta : "))
                        dados = (numero, cpf, 0.00, 1, dia_aniversario_conta)
                        sql = f'INSERT INTO {TABLE_NAME} (numero, cpf, saldo, ativa, diaAniversarioEspecial) VALUES (%s,%s,%s,%s,%s)'
                        cursor.execute(sql,dados)
                        conexao.commit()

                        sql =f'SELECT * FROM {TABLE_NAME}'
                        cursor.execute(sql)
                        resposta = cursor.fetchall()
                        print("Dados cadastrados")                    
                        for linha in resposta:
                            print(linha)
                    conexao.commit()
                    time.sleep(3)

                elif sub_opcao_menu == '2':  
                    numero_conta = int(input("Digite o número da conta que deseja alterar: "))
                    novo_cpf = input("Digite o novo CPF: ")
                    novo_dia_aniversario = int(input("Digite o novo dia de aniversário da conta: "))
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "Especial"
                        sql = f'UPDATE {TABLE_NAME} SET cpf=%s, diaAniversarioPoupanca=%s WHERE numero=%s'
                        cursor.execute(sql, (novo_cpf, novo_dia_aniversario, numero_conta))
                    conexao.commit()
                    print("Conta atualizada com sucesso!")
                    time.sleep(3)

                elif sub_opcao_menu == '3':  
                    numero_conta = int(input("Digite o número da conta que deseja apagar: "))
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "Especial"
                        sql = f'DELETE FROM {TABLE_NAME} WHERE numero=%s'
                        cursor.execute(sql, (numero_conta,))
                    conexao.commit()
                    print("Conta apagada com sucesso!")
                    time.sleep(3)


                elif sub_opcao_menu == '4':  
                    print("1 - Depositar")
                    print("2 - Sacar")
                    movimento = input("Digite sua opção: ")
                    numero_conta = int(input("Digite o número da conta: "))
                    valor = float(input("Digite o valor: "))
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "Especial"  
                        if movimento == '1':  
                            sql = f'UPDATE {TABLE_NAME} SET saldo=saldo+%s WHERE numero=%s'
                        elif movimento == '2':  
                            sql = f'UPDATE {TABLE_NAME} SET saldo=saldo-%s WHERE numero=%s AND saldo >= %s'
                    cursor.execute(sql, (valor, numero_conta, valor))
                    if cursor.rowcount == 0:
                        print("Saldo insuficiente!")
                    else:
                        print("Transação concluída com sucesso!")
                    conexao.commit()
                    time.sleep(3)

                elif sub_opcao_menu == '5': 
                    sair = True
                    break 

        elif opcao_menu_principal=='4':
            sair = True
            print("Saindo...")
            break 