# Python mundo 02
# Repetições em Python - IV
# Exercício 070 - Crie um programa que leia o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#   a) qual é o total gasto na compra
#   b) quantos produtos custam mais de R$1000,00
#   c) qual é o nome do produto mais barato.

c = 0
total = 0
msmil = 0
valbar = 0
barato = ''
res = 'SN'

print('\033[91m-\033[m' * 30)
print('\033[34m', 'LOJA SUPER BARATÃO'.center(30), '\033[m')
print('\033[91m-\033[m' * 30)

while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    c += 1

    # total da compra
    total += preco

    # preço maior que R$1000
    if preco > 1000:
        msmil += 1

    # produto mais barato
    if c == 1:
        barato = prod
        valbar = preco
    else:
        if preco < valbar:
            barato = prod
            valbar = preco

    # continuar e tratando erro
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while res not in 'SN':
        print('ERRO! Resposta inválida.')
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break

# dados finais
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {msmil} produto(s) custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custou R${valbar:.2f}')
print()
