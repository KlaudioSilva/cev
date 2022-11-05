# Python mundo 01
# Exercício 022 - Faça um programa que abra e reproduza um áudio mp3.
# Klaudio Silva.

from time import sleep
import pygame
from pygame.locals import *

pygame.init()

# indicando o arquivo de áudio
musica = pygame.mixer.music.load('boxcat_games_victory.mp3')

print('Tocando um áudio mp3.')
# dando o 'play' na música
pygame.mixer.music.play(-1)

sleep(50)  # dá um tempo de 50 segundos pra música tocar.
print('Pronto! Tchau')
print()
