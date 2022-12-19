# Python mundo 03
# Funções I em Python
# Exercício 100 - Faça um programa que tenha uma lista chamada 'numeros' e duas
# funções chamadas 'sorteia()' e 'somapar()'
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
# segunda função vai mostrar a soma entre todos os valores PARES sorteados
# pela função anterior.

from random import randint
numeros = []

def sorteia():  # sorteando os 5 valores
    for c in range(1, 6):
        numeros.append(randint(1, 9))


def somapar():  # somando apenas os valores que são pares
    tot = 0
    for c in numeros:
        if c % 2 == 0:
            tot += c
    print(f'Somando os valores pares de {numeros}, temos {tot}')


# programa principal
sorteia()
print(f'Sorteando 5 valores da lista: ', end='')
for c in numeros:
    print(c, end=' ')
print('PRONTO!')

somapar()
print('-' * 40)

'''
    Abaixo segue a solução proposta pelo Guanabara
'''

from time import sleep

def sorteia2(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somapar2(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

nums = list()
sorteia2(nums)
somapar2(nums)
print()
