def inicio():
    # Variáveis
    custoFabrica = 0.00
    custoConsumidor = 0.00
    porcentagemDistribuidor = 0.00
    percentualImposto = 0.00

    # Entradas
    custoFabrica = float(input("Digite o custo de fábrica do carro: "))

    # Processamentos
    porcentagemDistribuidor = custoFabrica * 0.28
    percentualImposto = custoFabrica * 0.45
    custoConsumidor = custoFabrica + porcentagemDistribuidor + percentualImposto

    # Saída
    print("\n28% do distribuidor: ", porcentagemDistribuidor)
    print("45% de imposto: ", percentualImposto)
    print("O custo ao consumidor é: ", custoConsumidor)

inicio()
