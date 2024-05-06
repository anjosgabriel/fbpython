import os

os.system('cls')

numero = int(input("Digite um número: "))

if (numero % 2 == 0) and (numero > 0):
    print("\nO número", numero, "é par e positivo.")

elif (numero % 2 == 0) and (numero < 0):
    print("\nO número", numero, "é par e negativo.")

elif numero == 0:
    print("\nO número", numero, "é neutro.")

elif (numero % 2 == 1) and (numero > 0):
    print("\nO número", numero, "é ímpar e positivo.")

else:
    print("\nO número", numero, "é ímpar e negativo.")