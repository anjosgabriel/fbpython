def inicio():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))

    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

    print("A média final do aluno é:", media)

inicio()
