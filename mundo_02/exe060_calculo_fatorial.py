# Python mundo 02
# Repetições em Python - III
# Exercício 059 - Faça um programa que leia um número qualquer
# e mostre o seu Fatorial: 
# EX: 5! = 5x4x3x2x1 = 120.

num = 0
fat = 1

num = int(input('''Digite um número para
calcular seu Fatorial: '''))

print('Calculando {}! = '.format(num), end='')  # fazendo com que o while continue nesta linha
while num > 0:  # enquanto o valor for maior que 0, continue fatorando e printando na mesma linha
    print('{}'.format(num), end='')
    fat = fat * num
    
    # escolhendo entre exibir o 'x' e o '='
    if num > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    num -= 1

# fatorial do número escolhido
print('{}'.format(fat))
print()
