# Python mundo 01
# Condições em Python
# Exercício 034 - Desenvolva um programa que leia o comprimento de três
# retas e diga ao usuário se elas podem formar ou não um triângulo.
# Klaudio Silva.

print('\033[96m-=\033[m' * 15)
print('Analisador de Triângulos'.center(30))
print('\033[96m-=\033[m' * 15)

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

# forma triângulo
if (seg1 + seg2 > seg3) and (seg1 + seg3 > seg2) and (seg2 + seg3 > seg1):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
# não forma triângulo
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
print()
