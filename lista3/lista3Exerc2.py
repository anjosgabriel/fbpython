import os

os.system('cls')

valores = range(1,501,3)
total = 0
for valor in valores: 
    if (valor%2 == 1):
        print(valor)
    total += valor 

print(f"Somatorio de numeros impares multiplos de 3 entre 1 e 500 é {total}")