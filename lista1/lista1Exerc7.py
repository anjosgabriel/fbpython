def inicio():
    A = int(input("Coeficiente A = "))
    B = int(input("Coeficiente B = "))
    C = int(input("Coeficiente C = "))
    D = int(input("Coeficiente D = "))
    E = int(input("Coeficiente E = "))
    F = int(input("Coeficiente F = "))

    x = ((C * E) - (B * F)) / ((A * E) - (B * D))
    print("O valor de X é:", x)

    y = ((A * F) - (C * D)) / ((A * E) - (B * D))
    print("O valor de Y é:", y)

inicio()
