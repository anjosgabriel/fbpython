dias_totais = int(input("Digite o total de dias : "))
anos = dias_totais // 365 
meses = int((dias_totais % 365)/30)
dias = int((dias_totais % 365)%30)
print(f"Anos : {anos}\nMeses : {meses}\nDias : {dias}")