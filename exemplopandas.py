import pandas as pd
import os

def cabeca():
    os.system("cls")
    print("-"*20,end='')
    print("Arquivo Vendas",end='')
    print("-"*20)


vendas_df = pd.read_excel("Vendas.xlsx")
pd.set_option('display.max_columns',None)

#faturamento por loja
cabeca()
print(vendas_df)