# Python mundo 02
# Condições em Python - II
# Exercício 044 - Crie um programa que faça o computador
# jogar 'Pedra, Papel ou Tesoura' com você.
# Klaudio Silva.

from time import sleep
from random import randint

print('-=-' * 10)
print('JOGO: JO KEN PO'.center(30))
print('-=-' * 10)

print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

opt = int(input('Qual é a sua jogada? '))

print()
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
print()

# itens do computador
com = randint(1, 3)
if com == 1:
    pc = 'Pedra'
elif com == 2:
    pc = 'Papel'
else:
    pc = 'Tesoura'

# itens do jogador
if opt == 1:
    jog = 'Pedra'
elif opt == 2:
    jog = 'Papel'
elif opt == 3:
    jog = 'Tesoura'
else:
    print('\033[31mESTÁ OPÇÃO É INVÁLIDA!\033[m')

print('-=' * 12)
print('Computador jogou {}'.format(pc))
print('Jogador jogou {}'.format(jog))
print('-=' * 12)

# quem vence?
if (com == 1):  # se o computador jogar PEDRA
    if opt == 1:
        print('EMPATE')
    elif opt == 2:
        print('JOGADOR VENCEU!')
    elif opt == 3:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif (com == 2):  # se o computador jogar PAPEL
    if opt == 2:
        print('EMPATE')
    elif opt == 1:
        print('COMPUTADOR VENCEU!')
    elif opt == 3:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif (com == 3):  # se o computador jogar TESOURA
    if opt == 3:
        print('EMPATE')
    elif opt == 1:
        print('JOGADOR VENCEU!')
    elif opt == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
print()
