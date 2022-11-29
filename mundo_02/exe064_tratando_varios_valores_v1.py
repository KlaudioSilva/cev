# Python mundo 02
# Repetições em Python - III
# Exercício 064 - Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de
# para. No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando o flag).

num = 0
totnum = 0
som = 0
while num != 999:  # continuar até digitar a condição de parada
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:  # se num for diferente de 999 faça:
        totnum += 1
        som = som + num

print(f'Você digitou {totnum} números e a soma entre eles foi {som}.')
print()
