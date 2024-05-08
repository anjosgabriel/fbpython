# listas

import os

os.system('cls')

lista = []
letras = list("EPAMINONDAS")
numeros = list(range(10))
print(lista)
print(letras)
print(numeros)

# como fazer para acessar o ultimo caracter da lista?

#print("Ultimo caracter da lista letras ",letras[-1])

# ou 

print("Ultimo caracter da lista numeros ",numeros[-1])
listanova = letras + numeros
print(listanova)
print("Tamanho da lista nova é ",len(listanova))

# como apagar o ultimo item da lista 7

listanova.pop()
print(listanova)
print("Tamanho da lista nova é ",len(listanova))

del listanova[10]
print(listanova)
print("Tamanho da lista nova é ",len(listanova))

# como adicionar algo na lista

listanova.append("EXEMPLO NA LISTA")
print(listanova)
print("Tamanho da lista nova é ",len(listanova))
listanova.insert(10,"s")
print(listanova)
print("Tamanho da lista nova é ",len(listanova))

listanova[10] = "S"
print(listanova)
print("Tamanho da lista nova é ",len(listanova))


for indice, item in enumerate(listanova):
    print(indice+1, item)