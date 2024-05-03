def inicio():
    A = int(input("numero A: "))
    B = int(input("numero B: "))
    C = int(input("numero C: "))
    
    R = (A + B) * (A + B)
    S = (B + C) * (B + C)
    
    D = (R + S) / 2
    
    print("resultado =", D)

inicio()
