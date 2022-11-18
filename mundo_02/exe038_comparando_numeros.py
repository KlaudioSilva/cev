# Python mundo 02
# Condições em Python - II
# Exercício 038 - Crie um programa que leia dois números inteiros e
# compare, mostrando na tela uma mensagem:
#   - o primeiro valor é maior
#   - o segundo valor é maior
#   - não existe maior, os dois são iguais.
# Klaudio Silva.

print('-' * 20)
print('QUAL É O MAIOR?'.center(20))
print('-' * 20)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O PRIMEIRO valor é o maior!')
elif n2 > n1:
    print('O SEGUNDO valor é o maior!')
else:
    print('NÃO existe maior, os valores são iguais!')
print()
