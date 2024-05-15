import pandas as pd
import os

def cabeca():
    os.system("cls")
    print("-"*20,end='')
    print("Arquivo Vendas",end='')
    print("-"*20)

feminicidio_df = pd.read_csv("Feminicidio.csv")
pd.set_option('display.max_columns',None)
print(feminicidio_df)
estatistica = feminicidio_df[['ANO_ESTATISTICA','VITIMAS']].groupby('ANO_ESTATISTICA').sum()
print(estatistica)
estatistica_raca = feminicidio_df[['COR_PELE','VITIMAS']].groupby('COR_PELE').sum()
print(estatistica_raca)
estatistica_departamento = feminicidio_df[['DEPARTAMENTO_CIRCUNSCRICAO','VITIMAS']].groupby('DEPARTAMENTO_CIRCUNSCRICAO').sum()
print(estatistica_departamento)
estatistica_municipio = feminicidio_df[['MUNICIPIO_CIRCUNSCRICAO','VITIMAS']].groupby('MUNICIPIO_CIRCUNSCRICAO').sum()
print(estatistica_municipio)
estatistica_profissao = feminicidio_df[['PROFISSAO','VITIMAS']].groupby('PROFISSAO').sum()
print(estatistica_profissao)