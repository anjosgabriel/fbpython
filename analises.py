import pandas as pd
import matplotlib.pyplot as plt 

import os

pd.set_option('display.max_columns', None)

#lendo a base de dados em um objeto 
df = pd.read_csv('Feminicidio.csv')
cidades = [
    'Santo André',
    'São Bernardo do Campo'
]

#Montagem imagem de osasco 
#cidade_df = df[df['MUNICIPIO_CIRCUNSCRICAO']=='Osasco']
cidade_df = ...

os.system('cls') # os.system('clear')

print('raca_df')