# Python mundo 01
# Condições em Python
# Exercício 028 - Crie um programa que escolha um número de 0 a 5 e faça
# o usuário tentar descobrir qual foi o número escolhido pelo programa.
# Na tela deverá aparecer um mensagem dizendo se o usuário venceu ou
# perdeu.
# Klaudio Silva.

# importanto bibliotecas
from random import randint
from time import sleep

print('\033[33m-=-\033[m' * 18)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 18)

# número escolhido pelo programa
num = randint(0, 5)

# chute do usuário
chute = int(input('Em que número eu pensei? '))

print('\033[35mPROCESSANDO...')
sleep(2)  # aguarde 2 segundos

# condição de vitório ou derrota
if chute == num:
    print('\033[32mPARABÉNS! Você consegui acertar!\033[m')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}!'.format(num, chute))
print()
