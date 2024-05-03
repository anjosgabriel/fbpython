total_numeros = 0

for x in range(1, 501):
    if x % 2 == 1 and x % 3 == 0:
        print(x)
        total_numeros += x

print("O Total:", total_numeros)
