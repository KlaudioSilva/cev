# Python mundo 03
# Lista II em Python
# Exercício 085 - Crie um programa onde o usuário possa digitar
# sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores Pares e Ímpares. No final, mostre
# os valores pares e ímpares em ordem crescente.

nums = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        nums[0].append(valor)
    else:
        nums[1].append(valor)
print('-=' * 15)
nums[0].sort()
nums[1].sort()
print(f'Os valores pares digitados foram: {nums[0]}')
print(f'Os valores ímpares digitados foram: {nums[1]}')
print()
