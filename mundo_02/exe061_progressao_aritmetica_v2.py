# Python mundo 02
# Repetições em Python - III
# Exercício 061 - Refaça o exercício 051, lendo o primeiro termo e
# a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura "while".

print('Gerador de PA'.center(20))
print('-=' * 10)

t1 = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
cont = 1
termo =  t1

while cont <= 10:  # enquanto o contador for menor que 10
    print('{} → '.format(termo), end='')  # exibir os termos na mesma linha
    termo += rz  # somando a razão
    cont += 1  # add mais um ao contador
print('Fim')
print()
