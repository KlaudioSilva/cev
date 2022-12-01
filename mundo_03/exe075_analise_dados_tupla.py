# Python mundo 03
# Tuplas em Python
# Exercício 075 - Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final mostre:
#   a- quantas vezes aparece o valor 9
#   b- em que posição foi digitado o primeiro 3
#   c- quais foram os números pares.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último núḿero: '))

nums = (n1, n2, n3, n4)
print(f'Você digitou os valores {nums}')

if 9 in nums:
    print(f'O valor 9 aparece {nums.count(9)} vez(es)')
else:
    print('O valor 9 não foi digitado nenhuma vez.')

if 3 in nums:
    print(f'O valor 3 apareceu na {nums.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado nenhuma vez')

print(f'Os valores pares digitados ', end='')
for c in nums:
    if c % 2 == 0:
        print(c, end=' ')