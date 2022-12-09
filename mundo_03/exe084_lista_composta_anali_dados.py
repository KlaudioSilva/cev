# Python mundo 03
# Lista II em Python
# Exercício 084 - Faça um programa que leia nome e peso de várias
# pessoas, guardando tudo em uma lista. No final, mostre:
#   a) quantas pessoas foram cadastradas
#   b) uma lista com as pessoas mais pesadas
#   c) uma lista com as pessoas mais leves.

grupo = []
dados = []
tot = kilo = maior = menor = 0  # inicando todas as variáveis numéricas juntas
res = 'SN'

while True:
    # dando entrada nos dados
    dados.append(str(input('Nome: ')))
    kilo = float(input('Peso: '))
    dados.append(kilo)
    grupo.append(dados[:])
    dados.clear()
    tot += 1

    # verificando maior e menor peso
    if tot == 1:
        maior = kilo
        menor = kilo
    else:
        if kilo > maior:
            maior = kilo
        if kilo < menor:
            menor = kilo

    res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Resposta Inválida! Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break

print('-=-' * 15)

# Apresentação da análise dos dados
print(f'Ao todo, você cadastrou {tot} pessoas.')

print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
# Nomes dos mais pesados
for i, p in grupo:
    if p == maior:
        print(f'{i}', end='... ')
print('\n')

print(f'O menor peso foi de {menor:.1f}Kg. Peso de ', end='')
# Nomes dos mais leves
for i, p in grupo:
    if p == menor:
        print(f'{i}', end='... ')
print('\n')
print()
