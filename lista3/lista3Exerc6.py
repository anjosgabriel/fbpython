import os

os.system('cls')

contador = 1
total = 0
numero = int(input("Digite um numero entre 2 e 9 :"))
while True:
    print(contador,end="+")
    contador=contador+1
    if contador > numero :
        break 

print('\nfim de programa')