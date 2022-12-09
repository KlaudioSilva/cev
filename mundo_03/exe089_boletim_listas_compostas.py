# Python mundo 03
# Lista II em Python
# Exercício 089 - Crie um programa que leia os nomes e duas notas de vários
# alunos e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

classe = []
aluno = []
med = 0
res = 'SN'

# inserindo os dados na lista alunos e copiando para a lista classe
while True:
    aluno.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    aluno.append(n1)
    n2 = float(input('Nota 2: '))
    aluno.append(n2)
    med = (n1 + n2) / 2
    aluno.append(med)
    classe.append(aluno[:])
    aluno.clear()

    res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Resposta inválida! Deseja continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break

print('-=-' * 20)
# número - nome - média do aluno
print(f'{"Nº":<5}{"NOME":<15}{"MÉDIA":>5}')  
print('-' * 30)

con = 0
for a in classe:
    # apresentando os dados devidamente alinhados
    print(f'{con:<5}{a[0]:<15}{a[3]:>5.1f}')
    con += 1
print('-' * 30)

while True:
    qual = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if qual == 999:
        print('FINALIZANDO!')
        break
    if qual <= len(classe) -1:  # exibindo o aluno requerido
        print(f'Notas de {classe[qual][0]} são {classe[qual][1]} e {classe[qual][2]}')

''' Com certeza eu este código, apesar de funcional, poderia ser escrito de forma muito mais limpa.
    Mas estou me propondo a criar meus próprios algoritmos para firma bem a minha lógica e gradativamente
    ir melhorando o meu código com algoritmos mais bem escritos e limpos.
    Para ajudar na fixação decidi deixar abaixo o algoritimo que foi usado no desafio do prof. Guanabara.
'''

print()
print('\033[31m-=-\033[m' * 25)
print('\033[36mAqui embaixo segue a lógica usada pelo professor Gustavo Guanabara:\033[m')

ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
