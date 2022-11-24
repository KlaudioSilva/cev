# Python mundo 02
# Repetições em Python - II
# Exercício 050 - Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o valor digitado for
# ímpar, desconsidere-o.
# Klaudio Silva.

print('=' * 20)
print('SOMA PARES'.center(20))
print('=' * 20)

soma = 0
totpar = 0

for c in range(1, 6 + 1):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        totpar += 1

print('Foram somados {} valores pares, o total é {}'.format(totpar, soma))
print()
