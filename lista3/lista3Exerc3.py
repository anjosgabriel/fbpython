numero = 0
contador = 0
soma = 0
media = 0

print("Digite um número:")
numero = int(input())

while numero > 0:
    contador += 1
    soma += numero
    media = soma / contador

    print("Digite um número:")
    numero = int(input())

print("\nSoma =", soma)
print("Contador =", contador)
print("Média =", media)
