# Python mundo 01
# Exercício 020 - Agora o professor quer sortear a ordem de apresentação
# de trabalho dos alunos.
# Faça um programa que leia os nomes e mostre a ordem sorteada.
# Klaudio Silva.

import random
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
alunos = [al1, al2, al3, al4]

print('A ordem de apresentação será:')
random.shuffle(alunos)
print(alunos)
print()
