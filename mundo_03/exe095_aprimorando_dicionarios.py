# Python mundo 03
# Dicionários em Python
# Exercício 095 - Aprimore o exercício 093, para que ele funcione
# com vários jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.

jog = {}
time = []
gols = []

while True:
    # recebendo os dados do jogador em um dicionario e inserindo na lita
    tot = 0
    jog['nome'] = str(input('Nome do Jogador: ')).strip()
    part = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
    for c in range(1, part+1):
        gols.append(int(input(f'  → Quantos gols na partida {c}? ')))

    for gol in gols:
        tot += gol

    jog['gols'] = gols[:]
    gols.clear()
    jog['total'] = tot
    time.append(jog.copy())

    res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Resposta Inválida! Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break


print('-=' * 30)
# cabeçalho de infos
print(f'cod ', end='')
for i in jog.keys():
    print(f'{i:<18}', end='')
print()
print('-' * 44)

# os jogadores e seus gols
for k, v in enumerate(time):
    print(f'{k:>2}', end=' ')
    for d in v.values():
        print(f'{str(d):<18}', end='')
    print()
print('-' * 44)

while True:
    cod = int(input('Mostrar os dados de qual jogador? (999 para terminar): '))  # qual jogador exibir
    if cod == 999:
        break
    if cod >= len(time):
        print(f'ERRO! Não existe jogador com o código {cod}!')
    else:  
        print(f'── LEVANTAMENTO DO JOGADOR {time[cod]["nome"]}:')
        # as partidas e os gols marcados em cada uma
        for i, v in enumerate(time[cod]['gols']):
            print(f'No jogo {i+1} fez {v} gols.')
    print('-' * 44)