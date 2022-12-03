# Python mundo 03
# Lista I em Python
# Exercício 081 - Crie um programa que leia vários números e
# coloque-os em uma lista. Depois disso, mostre:
#   a) quantos números foram digitados
#   b) a lista de valores, ordenada de forma decrescente
#   c) se o valor 5 foi digitado e está ou não na lista.

lista = []
res = 'SN'
totelem = 0  # poderia ter usado o 'len' para obter o tamanho da lista

while True:
    lista.append(int(input('Digite um valor: ')))
    totelem += 1

    res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Resposta inválida! Deseja continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break

print('-=' * 30)
print(f'Você digitou {totelem} elementos.')
lista.sort(reverse=True)  # revertendo a lista
print(f'Os valores em ordem decrescente são {lista}')

# encontrei ou não o 5 na lista
if 5 not in lista:
    print('O valor 5 não faz parte da lista!')
else:
    print('O valor 5 faz parte da lista!')
print()