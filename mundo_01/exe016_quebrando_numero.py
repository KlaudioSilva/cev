# Python mundo 01
# Exercício 016 - Crie um programa que leia um número real qualquer
# pelo teclado e mostre na tela a sua porção inteira.
# Ex:   Digite = 1.6245
#       Inteiro = 1
# Klaudio Silva.

from math import trunc
num = float(input('Digite um valor: '))

print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
print()
