import os

os.system('cls')

horas = 0
horas_excedente = 0
salario = 0.00

horas = int(input("Horas trabalhadas: "))

if horas > 50:
    horas_excedente = horas - 50
    salario = (horas_excedente * 20.00) + (10.00 * 50)
    print("Você trabalhou", horas, "horas.\nHouve um excesso de", horas_excedente, "horas.")
    print("Seu salário é de:", salario)
else:
    salario = horas * 10.00
    print("Você trabalhou", horas, "horas.")
    print("Seu salário é de:", salario)