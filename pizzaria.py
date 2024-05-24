import os

os.system('cls')

def menu_principal():
    print("Olá, tudo bem?\n")
    print("Seja Bem-Vindo à PIZZARIA DO GABRIEL!!!\n")
    print("Digite:\n")
    print("1 - Comprar pizza")
    print("2 - Sair\n")
    print("-" * 50)
def menu_pizzas():
    print("\nLista")
    print("1 - Mussarela - R$ 39,90")
    print("2 - Calabresa - R$ 41,50")
    print("3 - Frango - R$ 41,50")
    print("4 - Frango c/ Catupiry - R$ 43,50")
    print("5 - Atum - R$ 43,50")
    print("6 - Marguerita - R$ 43,50")
    print("7 - 2 Queijos - R$ 45,00")
    print("8 - Peperoni - R$ 45,00")
    print("9 - Chocolate - R$ 50,00")
    print("10 - Voltar ao Menu")
    print("-" * 50)
def obter_endereco():
    endereco = input("\nQual seu endereço? ")
    print(f"\nPedido confirmado! A pizza será entregue em: {endereco}\n")
    print("-" * 50)
def main():
    while True:
        menu_principal()
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            while True:
                menu_pizzas()
                escolha_pizza = input("\nEscolha sua pizza: ")

                if escolha_pizza in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    obter_endereco()
                    break
                elif escolha_pizza == '10':
                    break
                else:
                    print("\nOpção inválida, tente novamente.")

        elif escolha == '2':
            print("\nSaindo... Até a próxima!")
            break
        else:
            print("\nOpção inválida, tente novamente.")

if __name__ == "__main__":
    main()