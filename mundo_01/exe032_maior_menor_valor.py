# Python mundo 01
# Condições em Python
# Exercício 032 - Faça um programa que leia três números e mostre
# qual é o maior e qual é o menor valor.
# Klaudio Silva.

print('\033[31m-\033[m' * 30)
print('Qual é o Maior e o Menor'.center(30))
print('\033[31m-\033[m' * 30)

# entrada de valores
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

# calculando o maior
if (n1 > n2) and (n1 > n3):
    maior = n1
if (n2 > n1) and (n2 > n3):
    maior = n2
if (n3 > n1) and (n3 > n2):
    maior = n3
    
# calculado o menor
if (n1 < n2) and (n1 < n3):
    menor = n1
if (n2 < n1) and (n2 < n3):
    menor = n2
if (n3 < n1) and (n3 < n2):
    menor = n3

# apresentando o resultado
print('\033[91mO maior valor digitado foi {}.'.format(maior))
print('\033[94mO menor valor digitado foi {}.'.format(menor))
print()
