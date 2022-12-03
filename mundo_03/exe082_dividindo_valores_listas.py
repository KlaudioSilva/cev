# Python mundo 03
# Lista I em Python
# Exercício 082 - Crie um programa que vai ler vários números e
# colocá-los em uma lista.
# Depois disso crie duas listas extras que vão conter apenas os
# valores Pares e os valores Ímpares digitados respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
res = 'SN'
num = 0

while True:
    num = int(input('Digite um número: '))
    lista.append(num)  # lista completa

    if num % 2 == 0:
        pares.append(num)  # lista de pares
    else:
        impares.append(num)  # lista de ímpares

    res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Resposta inválida! Deseja continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break

print('=-' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de Pares é {pares}')
print(f'A lista de Ímpares é {impares}')
print()
