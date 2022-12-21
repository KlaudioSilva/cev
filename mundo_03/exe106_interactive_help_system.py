# Python mundo 03
# Funções II em Python
# Exercício 106 - Faça um mini-sistema que utilize o interactive help do
# Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa vai terminar.
# Obs: use cores.

from time import sleep
cores = ['\033[m',     # 0 - limpa
        '\033[1;41m',  # 1 - red
        '\033[1;42m',  # 2 - green
        '\033[1;43m',  # 3 - yellow
        '\033[1;44',   # 4 - blue
        '\033[7;30m',  # 5 - white
        '\033[1;45m'   # 6 - purple
        ]


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[5], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'{msg}'.center(tam))
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca → '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)