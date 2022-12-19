# Python mundo 03
# Funções I em Python
# Exercício 096 - Faça um programa que tenha uma função chamada
# 'area()', que receba as dimensões de um terreno retângular
# (largura e comprimento) e mostre a área do terreno.

# função que calcula a área de um terreno
def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l}x{c} é de {a:.1f}m².')

print('Controle de Terrenos'.center(30))
print('-' * 30)

# programa principal
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))
area(lar, com)  # chamando a função