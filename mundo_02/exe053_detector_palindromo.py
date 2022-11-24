# Python mundo 02
# Repetições em Python - II
# Exercício 053 - Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.
# Klaudio Silva.

frase = str (input('Digite uma frase: ')).upper().strip().split()
letra = ''.join(frase)
pali = ''
for l in range(len(letra) -1, -1, -1):
    pali += letra[l]
print('O inverso de {} é {}'.format(letra, pali))

if pali == letra:
    print('Temos um Palíndromo!')
else:
    print('Não temos um Palíndromo!')
print()