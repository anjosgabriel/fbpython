import os

os.system('cls')

def menu_principal():
    print("Olá, tudo bem?")
    print("\nDIGITE:")
    print("1 - Compra pizza")
    print("2 - Sair")
    print("-" * 50)
def menu_pizzas():
    print("\nLista")
    print("1 - Mussarela - R$ 50,00")
    print("2 - Calabresa - R$ 50,00")
    print("3 - Frango c/ Catupiry - R$ 50,00")
    print("4 - Voltar ao Menu")
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

                if escolha_pizza in ['1', '2', '3']:
                    obter_endereco()
                    break
                elif escolha_pizza == '4':
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