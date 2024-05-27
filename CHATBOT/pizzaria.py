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
    print("\nLista\n")
    print("Sabores Tradicionais\n")
    print("1 - Mussarela - R$ 35,00")
    print("2 - Calabresa - R$ 38,00")
    print("3 - Margherita - R$ 40,00")
    print("4 - Portuguesa - R$ 45,00")
    print("5 - Frango com Catupiry - R$ 42,00")
    print("6 - Quatro Queijos - R$ 48,00")
    print("7 - Atum - R$ 45,00")
    print("\nSabores Especiais\n")
    print("8 - Pepperoni - R$ 50,00")
    print("9 - Palmito - R$ 52,00")
    print("10 - Vegetariana - R$ 48,00")
    print("11 - Toscana - R$ 50,00")
    print("12 - Camarão - R$ 65,00")
    print("13 - Parma e Rúcula - R$ 55,00")
    print("14 - Lombo com Catupiry - R$ 52,00")
    print("\nSabores Doces\n")
    print("15 - Chocolate - R$ 38,00")
    print("16 - Chocolate com Morango - R$ 45,00")
    print("17 - Banana com Canela - R$ 35,00")
    print("18 - Romeu e Julieta (goiabada com queijo) - R$ 40,00")
    print("\nSabores Gourmet\n")
    print("19 - Brie com Damascos - R$ 70,00")
    print("20 - Parmesão com Mel - R$ 65,00")
    print("21 - Funghi - R$ 60,00")
    print("22 - Palmito - R$ 52,00")
    print("23 - Trufas Negras - R$ 90,00")
    print("24 - Voltar ao Menu")
    print("-" * 50)
def obter_endereco():
    endereco = input("\nQual seu endereço? ")
    print(f"\nPedido confirmado! A pizza será entregue na: {endereco}\n")
    print("-" * 50)
def main():
    while True:
        menu_principal()
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            while True:
                menu_pizzas()
                escolha_pizza = input("\nEscolha sua pizza: ")

                if escolha_pizza in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']:
                    obter_endereco()
                    break
                elif escolha_pizza == '24':
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