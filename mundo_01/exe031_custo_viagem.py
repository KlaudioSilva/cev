# Python mundo 01
# Condições em Python
# Exercício 031 - Crie um programa que pergunte a distância de uma
# passagem, cobrando R$0,50 para cada quilômetro em viagens até 200
# quilômetros e R$0,45 para viagens mais longas.
# Klaudio Silva.

viagem = int(input('Qual é a distância da sua viagem [Kms]? '))
print('Você está preste a começar uma viagem de {}kms.'.format(viagem))

if viagem <= 200:
    totviagem = viagem * 0.50  # viagem igual ou menor a 200km
else:
    totviagem = viagem * 0.45  #  viagem mais longa do que 200km

print('E o preço da sua passagem será de R${:.2f}.'.format(totviagem))
print()
