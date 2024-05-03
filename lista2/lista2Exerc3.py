import math

def inicio():
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    num3 = float(input("Digite o terceiro numero: "))
    num4 = float(input("Digite o quarto numero: "))
    
    num1Pot = math.pow(num1, 2)
    num2Pot = math.pow(num2, 2)
    num3Pot = math.pow(num3, 2)
    num4Pot = math.pow(num4, 2)
    
    if num3Pot >= 1000:
        print("\nO quadrado do terceiro número é", num3Pot, "sendo maior que mil.")
    else:
        print("\nO numero do quadrado", num1, "é", num1Pot)
        print("O numero do quadrado", num2, "é", num2Pot)
        print("O numero do quadrado", num3, "é", num3Pot)
        print("O numero do quadrado", num4, "é", num4Pot)

inicio()
