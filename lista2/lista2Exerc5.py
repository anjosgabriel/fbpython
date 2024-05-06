import os

os.system('cls')

indicePoluicao = 0.00

indicePoluicao = float(input("Qual o índice de poluição? "))

if indicePoluicao >= 0.3 and indicePoluicao < 0.4:
    print("\nÍndice de poluição é de:", indicePoluicao, "por isso as indústrias do primeiro grupo precisam suspender as atividades")
elif indicePoluicao >= 0.4 and indicePoluicao < 0.5:
    print("\nÍndice de poluição é de:", indicePoluicao, "por isso as indústrias do primeiro e segundo grupo precisam suspender as atividades")
elif indicePoluicao >= 0.5:
    print("\nÍndice de poluição é de:", indicePoluicao, "por isso as indústrias do primeiro, segundo e terceiro grupo precisam suspender as atividades")
else:
    print("\nÍndice de poluição aceitável.")
