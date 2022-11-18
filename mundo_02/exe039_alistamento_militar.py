# Python mundo 02
# Condições em Python - II
# Exercício 039 - Faça um programa que leia o ano de nascimento de 
# um jovem e informe, de acordo com a sua idade:
#   - se ele ainda vai se alistar ao serviço militar
#   - se já é a hora de se alistar
#   - se já passou do tempo de alistamento
# O programa também deverá mostrar o tempo que falta ou que passou do prazo.
# Klaudio Silva.

from datetime import date

nasc = int(input('Ano de nascimento: '))

atual = (date.today().year)  # ano atual
idade = atual - nasc         # sua idade

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade > 18:  # já passou da hora de se alistar
    print('Você já deveria ter se alistado há {} anos.'.format((atual - nasc) - 18))
    print('Seu alistamento foi em {}.'.format(nasc + 18))
elif idade < 18:  # ainda é cedo para se alistar
    print('Ainda falta(m) {} ano(s) para o alistamento'.format(18 - (atual - nasc)))
    print('Seu alistamento será em {}.'.format(nasc + 18))
else:  # seu alistamento é esse ano
    print('Você tem que se alistar IMEDIATAMENTE!')
print()
