# Python mundo 03
# Lista I em Python
# Exercício 080 - Crie um programa onde o usuário pode digitar cinco valores
# numéricos e cadastre-os em uma lista já na posição correta de inserção (sem
# usar o 'sort').
# No final, mostre a lista ordenada na tela.

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:  # add no inicio da lista
        lista.append(n)
    elif n > lista[-1]:  # add no final da lista
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)  # add na posição {pos} da lista
                break
            pos += 1

print('-=-' * 15)
print(f'Os valores digitados em ordem foram {lista}')
print()
