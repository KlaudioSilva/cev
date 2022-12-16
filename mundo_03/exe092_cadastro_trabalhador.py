# Python mundo 03
# Dicionários em Python
# Exercício 092 - Crie um programa que leia nome, ano de nascimento,
# carteira de trabalho (ctps) e cadastre-os (com idade) em um dicionário. Se
# por acaso a ctps for diferente de zero, o dicionário receberá também o ano
# de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
ano = (date.today().year)
cad = {}
cad['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cad['idade'] = ano - nasc
cad['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cad['ctps'] > 0:
    cad['contratacão'] = int(input('Ano de Contratação: '))
    cad['salário'] = float(input('Salário: R$'))
    cad['aposentadoria'] = (cad['contratacão'] - nasc) + 35
print('-=' * 20)
for k, v in cad.items():
    print(f'─ {k} tem o valor {v}')
print()
print(cad)