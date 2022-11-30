# Python mundo 02
# Repetições em Python - IV
# Exercício 066 - Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai para quando o usuário digitar o valor: 999,
# que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (Desconsidando o Flag).

cont = 0
som = 0

while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    som = som + num

print(f'A soma dos {cont} valores foi {som}.')
print()
