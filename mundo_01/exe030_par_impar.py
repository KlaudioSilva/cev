# Python mundo 01
# Condições em Python
# Exercício 030 - Crie um programa que leia um número inteiro
# e mostre se ele é PAR ou ÍMPAR.
# Klaudio Silva.

num = int(input('\033[95mMe diga um número qualquer:\033[m '))

if num % 2 == 0:
    print('O número {} é \033[94mPAR\033[m!'.format(num))
else:
    print('O número {} é \033[91mÍMPAR\033[m!'.format(num))
print()
