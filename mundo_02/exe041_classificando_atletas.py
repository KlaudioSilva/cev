# Python mundo 02
# Condições em Python - II
# Exercício 041 - A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo
# com a sua idade:
#   ─ até 9 anos: mirim
#   ─ até 14 anos: infantil
#   ─ até 19 anos: júnior
#   ─ até 20 anos: sênior
#   ─ acima: master.
# Klaudio Silva.

from datetime import date

nasc = int(input('Ano de Nascimento: '))
idade = (date.today().year) - nasc

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    cat = 'MIRIM'
elif (idade > 9) and (idade <=14):
    cat = 'INFANTIL'
elif (idade > 14) and (idade <= 19):
    cat = 'JÚNIOR'
elif idade == 20:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'

print('Classificação: {}!'.format(cat))
print()
