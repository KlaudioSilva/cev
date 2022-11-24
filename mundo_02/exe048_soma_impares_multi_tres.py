# Python mundo 02
# Repetições em Python - II
# Exercício 048 - Crie um programa que calcule a soma entre todos
# os números ímpares que são múltiplos de três e que se encontram
# no intervalo entre 1 e 500.
# Klaudio Silva.

soma = 0
totval = 0
for c in range(1, 500):  # no intervalo de 1 a 500
    if c % 2 == 1:       # se o contador for um valor ímpar
        if c % 3 == 0:   # se o contador for um múltiplo de 3
            soma += c    # some os valores do contador
            totval += 1  # quantos valores já foram encontrados

print('A soma de todos os {} valores solicitados é {}.'.format(totval, soma))
print()
