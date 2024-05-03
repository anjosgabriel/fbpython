def inicio():
    peso = int(input("Digite o peso: "))
    excesso = 0
    multa = 0

    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        print("O excesso é de:", excesso, "kg.")
        print("Multa de 4 reais por excesso, no total de:", multa, "reais.")
    else:
        print("Peso não excede!")

inicio()
