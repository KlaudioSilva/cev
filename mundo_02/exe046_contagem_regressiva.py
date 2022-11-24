# Python mundo 02
# Repetições em Python - II
# Exercício 046 - Faça um programa que mostre na tela uma contagem regressiva para o
# estouro de fogos de artifícios, indo de 10 a 0, com uma pausa de 1 segundo
# entre cada número.
# Klaudio Silva.

from time import sleep
print('Contagem Regressiva')
print('-------------------')

for c in range(10, -1, -1):  # para o contador no intervalo de 10 a -1, tire 1
    print(c)
    sleep(1)  # aguarde 1 segundo
print('BOOM! BOOM! KABUMM!')
print()
