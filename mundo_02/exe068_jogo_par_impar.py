# Python mundo 02
# Repetições em Python - IV
# Exercício 068 - Faça um programa que jogue Par ou Ímpar com o computador.
# O programa do jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

vit = 0
deu = ''

# números do computador e do jogador e escolha de par ou impar
while True:
    cpu = randint(1, 9)
    num = int(input('Diga um valor: '))
    jogada = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    # soma das escolhas e resultado par/ímpar
    res = num + cpu
    if res % 2 == 0:
        deu = 'PAR'
    else:
        deu = 'ÍMPAR'

    print('-' * 30)
    # resultados
    print(f'Você jogou {num} e o computador {cpu}. Total de {res} DEU {deu}.')
    
    # quem venceu
    if ((deu == 'PAR') and (jogada == 'P')) or ((deu == 'ÍMPAR') and (jogada == 'I')):
        vit += 1
        print('Você VENCEU! \nVamos jogar novamente...')
    if ((deu == 'PAR') and (jogada == 'I')) or ((deu == 'ÍMPAR') and (jogada == 'P')):
        print('Você PERDEU!')
        break

print('=-' * 15)
print(f'GAME OVER! Você venceu {vit} vezes.')
print()
