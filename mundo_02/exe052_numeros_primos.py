# Python mundo 02
# Repetições em Python - II
# Exercício 052 - Faça um programa que leia um número inteiro e diga
# se ele é ou não um número primo.
# Klaudio Silva.

num = int(input('Digite um número: '))
totdiv = 0

for c in range(1, num + 1):
    if num % c == 0:
        totdiv += 1
        print('\033[91m', end='')
    else:
        print('\033[34m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divísvel {} vezes.'.format(num, totdiv))
if totdiv == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')
print()
