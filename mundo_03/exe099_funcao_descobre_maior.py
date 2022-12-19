# Python mundo 03
# Funções I em Python
# Exercício 099 - Faça um programa que tenha uma função chamada 'maior()', que
# receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
from time import sleep

# função que descobre o maior valor
def maior(num):
    mai = 0
    print('-=-' * 15)
    print('Analisando os valores pasados...')

    for n in (num):
        if n > mai:
            mai = n
        print(f'{n}', end=' ')
        sleep(0.5)
    print(f'foram informados {len(num)} números.')
    print(f'O maior valor informado foi {mai}.')


# programa principal
valores = []
cont = 0
print('-=-' * 15)

while cont != 5:
    c = 0
    tam = randint(0, 7)
    while c < tam:
        valores.append(randint(0, 10))
        c += 1
    maior(valores)
    valores.clear()
    cont += 1
print()
