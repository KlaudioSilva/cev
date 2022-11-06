# Python mundo 01
# Usando Módulos
# Exercício 023 - Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos digitos separados. Ex: 1834
#   unidade → 4
#   dezena  → 3
#   centena → 8
#   milhar  → 1
# Klaudio Silva.

num = int(input('Digite um valor inteiro entre 0 e 9999: '))

# separando os digitos
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

# apresentando o resultado
print('Analisando o número {}'.format(num))
print('Unidade = {}'.format(uni))
print('Dezena  = {}'.format(dez))
print('Centena = {}'.format(cen))
print('Milhar  = {}'.format(mil))
print()
