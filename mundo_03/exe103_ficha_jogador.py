# Python mundo 03
# Funções II em Python
# Exercício 103 - Crie um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos
# gols ele marcou.
# O programa deve ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.

def ficha(nome = '<desconhecido>', gol = 0):
    print(f'O jogador {nome} fez {gol} gols no campeonato.')


jog = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():  # se a var gols é um valor numérico
    gols = int(gols)  # transforma em inteiro
else:
    gols = 0  # recebe um 0
if jog.strip() == '':  # se o nome do jogador está vazio
    ficha(gol=gols)  # apenas gol recebe os gols
else:
    ficha(jog, gols)  # nome e qtd de gols
