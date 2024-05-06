import os

os.system('cls')

# montagem da lista

lista = [1, 1.34,"texto",("1",2,"oi"), []]

aluno = {
    'matricula': 1,
    'nome': "Epaminondas",
    'nascimento': 2000,
    'turma': 'tecnico'
}

aluno2 = {
    'matricula': 2,
    'nome': "Maria",
    'nascimento': 2001,
    'turma': 'administração'
}
lista.append(aluno)
lista.append(aluno2)

# print(lista)

for nomes in lista:
    for chave in nomes: 
        print(f"{chave} : {nomes[chave]}")