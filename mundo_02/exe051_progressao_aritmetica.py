# Python mundo 02
# Repetições em Python - II
# Exercício 051 - Escreva um programa que leia o primeiro termo e a razão
# de uma progressão aritmética. No final, mostre os 10 primeiros termos
# dessa progressão.
# Klaudio Silva.

print('\033[35m-+-\033[m' * 10)
print('\033[96m', '10 TERMOS DE UMA PA'.center(30), '\033[m')
print('\033[35m-+-\033[m' * 10)
t1 = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
decimo = t1 + (10 - 1) * raz

for c in range(t1, decimo + raz, raz):
    print(c, end=' → ')
print('ACABOU')
print()
