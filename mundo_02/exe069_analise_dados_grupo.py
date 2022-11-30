# Python mundo 02
# Repetições em Python - IV
# Exercício 069 - Crie um programa que leia a idade e o sexo de várias
# pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o 
# usuário quer ou não continuar.

sexo = 'MF'
res = 'SN'
dezoito = 0
tothom = 0
mulhvint = 0

while True:
    print('-' * 24)
    print('CADASTRE UMA PESSOA'.center(24))
    print('-' * 24)

    # entrada de dados
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    # tratando o erro na digitação do sexo
    while sexo not in 'MF':
        print('ERRO! Use M ou F para definir o sexo.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 24)

    # somando 1 às variáveis 
    if idade > 18:
        dezoito += 1
    if sexo == 'M':
        tothom += 1
    if (idade < 20) and (sexo == 'F'):
        mulhvint += 1

    # vai continuar e tratamento de erro da resposta
    res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while res not in 'SN':
        print('ERRO! Resposta inválida.')
        res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if res == 'N':
        break

# resultados finais
print(f'Total de pessoas com mais de 18 anos → {dezoito}')
print(f'Ao todo temos {tothom} homem(ns) cadastrado(s)')
print(f'E temos {mulhvint} mulher(es) com menos de 20 anos')
print()
