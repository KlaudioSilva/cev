# Python mundo 02
# Repetições em Python - II
# Exercício 047 - Crie um programa que mostre na tela todos os
# números pares que estão no intervalo entre 1 e 50.
# Klaudio Silva.

print('\033[33m-\033[m' * 30)
print('\033[34m', 'EXIBINDO OS PARES'.center(30), '\033[m')
print('\033[33m-\033[m' * 30)

for c in range(0, 50 + 2):
    if c % 2 == 0:  # se o valor do contador for PAR
        print(c, end=' ')  # tudo na mesma linha
print('Acabou!')
print()
