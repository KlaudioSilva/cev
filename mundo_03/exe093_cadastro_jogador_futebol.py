# Python mundo 03
# Dicionários em Python
# Exercício 093 - Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois de ler a
# quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.

# iniciando as lista e a variável
jog = {}
gols = []
tot = 0

# entrando com os dados nome, qtd partidas e gols p/ partida
jog['nome'] = str(input('Nome do Jogador: ')).strip()
part = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
for c in range(1, part+1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
for gol in gols:
    tot += gol  # totalizando os gols

print(gols)
jog['gols'] = gols  # adic a lista de gols
jog['total'] = tot  # o total dos gols
print('-=' * 30)
print(jog)
print('-=' * 30)

for k, v in jog.items():
    print(f'O campo {k} tem o valor {v}')  # apresentando a tabela de infos básicas

print('-=' * 30)
print(f'O jogador {jog["nome"]} jogou {part} partidas.')

c = 1
'''
# obs: eu poderia ter usado a função 'enumerate' aqui, mas me esqueci dessa possibilidade
for i, v in enumerate(jog['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
'''
for g in gols:
    print(f'    => Na partida {c}, fez {g} gol(s).')  # apresentando a tabela com as partidas e seus gols
    c += 1

print(f'Foi um total de {tot} gols.')
print()