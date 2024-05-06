import os

os.system('cls')

base = float(input("Digite o tamanho da base: "))
altura = float(input("Digite o tamanho da altura: "))

if base > 0 and altura > 0:
    area_tri = (base * altura) / 2
    print("A base mede:", base)
    print("A altura mede:", altura)
    print("A área do triângulo é de:", area_tri)
else:
    print("Os valores não correspondem!")