# Python mundo 01
# Exercício 019 - Um professor quer sortear um dos seus alunos para
# apagar o quadro. Faça um programa que ajude ele, lendo os nomes e
# mostrando o nome escolhido.
# Klaudio Silva.

import random
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
lista = [al1, al2, al3, al4]

escolha = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolha))
print()
