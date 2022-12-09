# Python mundo 03
# Lista II em Python
# Exercício 088 - Faça um programa que ajude um jogador da Mega Sena
# a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('-' * 40)
print('JOGA NA MEGA SENA'.center(40))
print('-' * 40)

jogos = []
nums = []

totjogos = int(input('Quantos jogos você quer que eu sorteie? '))  # escolha quantos jogos
print(f'-=-=-=  SORTEANDO {totjogos} JOGOS  =-=-=-')

while totjogos > 0:  # enquanto o total de jogos não foi atinjido
    for n in range(1, 7):
        nums.append(randint(1, 60))  # sorteando os números
    jogos.append(nums[:])  # copiando para a lista jogos
    nums.clear()  # limpando a lista interna
    totjogos -= 1

for cont in range(0, len(jogos)):  # organizando a exibição dos palpites de jogos
    print(f'Jogo {cont+1}: {jogos[cont]}')
    sleep(1)
print()

print('\033[31m-=-\033[m' * 20)
print('\033[95mMesmo programa, mas sem os erros de repetições de números.\033[m')
print()

lista = []
jogos = []
quant = int(input('Quantos jogos devo sortear? '))
tot = 1
while tot <= quant:
    con = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            con += 1
        if con >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')
    print()

print('-=' * 5, '< BOA SORTE >', '-=' * 5)
print()