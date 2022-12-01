# Python mundo 03
# Tuplas em Python
# Exercício 074 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
# valor que estão na tupla.

from random import randint
valores = (randint(1, 9), randint(1,9), randint(1, 9), randint(1, 9), randint(1, 9))
print(f'Os valores sorteados foram: {valores}')

print(f'O mairo valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
print()
