# Python mundo 03
# Dicionários em Python
# Exercício 091 - Crie um programa onde 4 jogadores joguem um dado e tenham
# resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário
# em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

game = {}
c = 1

for j in range(1, 5):  # cada jogador joga o dado :)
    game['jogador' + str(j)] = randint(1, 6)

print('Valores Sorteados:')
sleep(0.5)
for k, v in game.items():  # exibindo os pontos de cada jogador
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
print('-=' * 15)

print('== RANKING DOS JOGADORES =='.center(31))
# o dicionario game2 recebe os valores de game em ordem do maior para o menor
game2 = dict(sorted(game.items(),key=lambda item: item[1], reverse=True))
for k, v in game2.items():
    print(f'{c}º lugar: {k} com {v}.')  # exibindo a colocação do jogadores
    c += 1
    sleep(1)
print()
