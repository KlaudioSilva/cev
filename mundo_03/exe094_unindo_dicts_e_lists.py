# Python mundo 03
# Dicionários em Python
# Exercício 094 - Crie um programa que leia nome, sexo e idade de
# várias pessoas, guardando os dados de cada pessoa em um dicionário,
# e todos os dicionários em uma lista. No final, mostre:
#   a) quantas pessoas foram cadastradas
#   b) a média de idade de grupo
#   c) uma lista com todas as mulheres
#   d) uma lista com todas as pessoas com idade acima da média.

pessoa = {}
grupo = []
totid = 0
cont = 0

# recebendo os dados
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    sex = str(input('Sexo: [M/F] ')).strip().upper()[0]
    # tratamento do sexo
    while sex not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        sex = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['sexo'] = sex
    pessoa['idade'] = int(input('Idade: '))
    totid += pessoa['idade']

    grupo.append(pessoa.copy())
    cont += 1

    res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    # tratamento do continue
    while res not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break

med = totid / cont
print('-=' * 30)
# apresentando a exibição final dos dados
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {med:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print(f'\nD) Lista das pessoas que estão acima da média:')
for p in grupo:  
    if p['idade'] >= med:  # cada pessoa na lista acima da média de idade
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')  # os dados de cada pessoa
        print()
print('<< ENCERRADO >>')
print('\n')