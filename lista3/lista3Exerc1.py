qtde = int(input("Digite o numero de habitantes : "))
HABITANTES = range(qtde)
salario = 0.00
total_salario = 0.00
numero_filhos = 0.00
total_filhos = 0.00
media_salarial = 0.00
media_filhos = 0.00
percentual_salario_1000 = 0.00
contador_salario_1000 = 0

for pessoa in HABITANTES:
    print("Habitante ",(pessoa+1))
    salario = float(input("Digite o salario : "))
    numero_filhos = int(input("Digite o numero de filhos : "))

    total_salario = total_salario + salario
    total_filhos = total_filhos + numero_filhos

media_salarial = total_salario / qtde
media_filhos = total_filhos / qtde

print(f"Total de salarios R$ {total_salario}")
print(f"Media salarial R$ {media_salarial}")
print(f"Total de filhos R$ {media_filhos}")

print("Fim de programa")