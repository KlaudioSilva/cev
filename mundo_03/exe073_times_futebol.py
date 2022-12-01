# Python mundo 03
# Tuplas em Python
# Exercício 073 - Crie uma tupla preenchida com os 20 primeiros colocados da
# tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
#   a) apenas os 5 primeiros colocados
#   b) os 4 últimos colocados da tabela
#   c) uma lista com os times na ordem alfabética
#   d) em que posição na tabela está o time do São Paulo.

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')

print('-=-' * 12)
print(f'Lista de times do Brasileirão 2022: {times}')
print('-=-' * 12)
print(f'Os 5 primeiros times da tabela são: {times[:5]}')
print('-=-' * 12)
print(f'Os 4 últimos times da tablea são : {times[-4:]}')
print('-=-' * 12)
print(f'Todos os times na ordem alfabética: {sorted(times)}')
print('-=-' * 12)
print(f'O time do São Paulo está na {times.index("São Paulo")+1}ª posição.')
print('-=-' * 12)
print()
