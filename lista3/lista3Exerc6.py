numero = 0
soma = 0

print("Digite um numero:")
limite = int(input())

while True:
    numero += 1
    soma += numero
    print(numero, end="")
    if numero == limite:
        break
    print("+", end="")

print(" =", soma)
