# Python mundo 03
# Dicionários em Python
# Exercício 090 - Faça um programa que leia nome e média de um
# aluno, guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.

aluno = {}
# recebendo os dados do dicionário
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-=' * 15)
print(f'─ nome é igual a {aluno["nome"]}')
print(f'─ média é igual a {aluno["media"]}')

# condicionais para aprovação
if (aluno['media'] <= 7) and (aluno['media'] > 5):
    sit = 'Recuperação'
elif (aluno['media'] <= 5):
    sit = 'Reprovado'
else:
    sit = 'Aprovado'

print(f'─ situação é igual a {sit}')
print('\n\n')


'''
Algoritmo usado pelo Guanabara:
'''
aluno1 = dict()
aluno1['nome'] = str(input('Nome: '))
aluno1['media'] = float(input(f'Média de {aluno1["nome"]}: '))

if aluno1['media'] >= 7:
    aluno1['situacao'] = 'Aprovado'
elif 5 <= aluno1['media'] < 7:
    aluno1['situacao'] = 'Recuperação'
else:
    aluno1['situacao'] = 'Reprovado'
print('-=' * 30)

for k, v in aluno1.items():
    print(f'─ {k} é igual a {v}')
