# Python mundo 02
# Repetições em Python - III
# Exercício 058 - Melhore o jogo do exercício 028, onde o computador vai
# "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando
# quantos palpites foram necessários para vencer.

from random import randint

print('\033[33m-+-\033[m' * 10)
print(f"\033[34m{'JOGO DA ADIVINHAÇÃO v2.0': ^30}\033[m")
print('\033[33m-+-\033[m' * 10)

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

cpu = randint(0, 10)  # número gerado pelo computador
paps = 0  # quantidade de palpites
chute = int(input('\033[94mQual é o seu palpite →\033[m '))

# enquanto o chute for diferente da nº da cpu...
while chute != cpu:
    if chute < cpu:
        print('Mais... Tente outra vez.')
    if chute > cpu:
        print('Menos... Tente outra vez.')
    chute = int(input('\033[94mQual é o seu palpite →\033[m '))
    paps += 1

print('\033[35mAcertou com {} tentativas. Parabéns!\033[m'.format(paps))
print()
