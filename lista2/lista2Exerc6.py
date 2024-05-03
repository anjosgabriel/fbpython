while True: 

    try:
        idade = int(input("Digite a idade : ")) 
        if idade < 5 : 
            print("Não atendemos nesta faixa etaria!!!")
        elif idade < 8:  
            print('Infantil A')
        elif idade < 12:
            print('Infantil B')
        elif idade < 14: 
            print('Juvenil A')
        elif idade < 18: 
            print('Juvenil B')
        else:
            print('Adulto')
    except: 
        print('Você não digitou uma idade valida')

    op = input("Continua S/N :").upper()
    if op == 'N' :
        break
print('Fim de programa')