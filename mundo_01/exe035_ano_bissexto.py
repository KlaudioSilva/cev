# Python mundo 01
# Condições em Python
# Exercício 035 - Faça um programa que leia um ano qualquer
# e mostre se ele é bissexto.
# Klaudio Silva.

from datetime import date

ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))

# pega o ano atual
if ano == 0:
    ano = date.today().year

# bissexto
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('O ano de {} é \033[34mBISSEXTO\033[m!'.format(ano))
# não bissexto
else:
    print('O ano de {} \033[31mNÃO é BISSEXTO\033[m!'.format(ano))
print()
