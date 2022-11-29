# Python mundo 02
# Repetições em Python - III
# Exercício 063 - Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma sequência Fibonacci.
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8...

from time import sleep

print('-' * 30)
print('Sequência de Fibonacci v1.0'.center(30))
print('-' * 30)

n1 = 0
n2 = 1
n3 = 0
con = 3  # o contador vai iniciar do 3
tot = 0

tot = int(input('Quantos termos você quer mostrar? '))
print('~' * 50)

print(n1, end=' → ')
sleep(0.5)
print(n2, end=' → ')
sleep(0.5)

while con <= tot:  # enquanto o contador for menor que o total de termos
    con += 1
    n3 = n1 + n2
    print(n3, end=' → ')
    sleep(0.5)
    n1 = n2  #  a variável n1 agora recebe o valor de n2
    n2 = n3  #  a variável n2 agora recebe o valor de n3
print('Fim!')
print('~' * 50)
print()
