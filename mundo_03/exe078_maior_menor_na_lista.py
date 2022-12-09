# Python mundo 03
# Lista I em Python
# Exercício 078 - Faça um programa que leia 5 valores numéricos e guarde-os
# em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e suas respectivas
# posições na lista.

valores = []
maior = menor = 0

for cont in range(0, 5):  # contador simples de 0 a 5
    num = (int(input(f'Digite um valor para a posição {cont}: ')))  # entrando um valor
    valores.append(num)  # adicionando esse valor à lista

    # estrutura para decidir o maior e o menor
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
            pos = cont
        if num < menor:
            menor = num
            pos = cont

print('=-=' * 15)

# apresentando os dados finais
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(valores):  # para cada item em valor enumere
    if v == maior:  # se o valor for igual a maior
        print(f'{i}...', end='')  # exibir o item(s), na mesma linha
        
print(f'\nO menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')

print()
