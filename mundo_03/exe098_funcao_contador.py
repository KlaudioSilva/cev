# Python mundo 03
# Funções I em Python
# Exercício 098 - Faça um programa que tenha uma função chamada 'contador()', que
# receba três parâmetros: início, fim e passo - e que realize a contagem.
# Seu programa tem de realizar três contagens através da função criada:
#   a) de 1 até 10, de 1 em 1
#   b) de 10 até 0, de 2 em 2
#   c) uma contagem personalizada.

from time import sleep

def contador(ini, fim, pas):
    print('-=-' * 15)
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
    sleep(0.5)

    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1

    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += pas
        print('FIM!')
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= pas
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-=-' * 15)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)