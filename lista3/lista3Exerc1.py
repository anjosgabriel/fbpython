salarios = []
num_filhos = []

for i in range(3):
    salario = float(input("Digite o salário do habitante {}: R$ ".format(i+1)))
    num_filho = int(input("Digite o número de filhos do habitante {}: ".format(i+1)))
    salarios.append(salario)
    num_filhos.append(num_filho)

media_salario = sum(salarios) / len(salarios)

media_filhos = sum(num_filhos) / len(num_filhos)

maior_salario = max(salarios)

pessoas_ate_100 = sum(1 for salario in salarios if salario <= 100)
percentual_ate_100 = (pessoas_ate_100 / len(salarios)) * 100

print("\nResultados:")
print("Média do salário da população: R$ {:.2f}".format(media_salario))
print("Média do número de filhos: {:.2f}".format(media_filhos))
print("Maior salário: R$ {:.2f}".format(maior_salario))
print("Percentual de pessoas com salário até R$100,00: {:.2f}%".format(percentual_ate_100))
