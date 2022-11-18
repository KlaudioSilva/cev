# Python mundo 02
# Condições em Python - II
# Exercício 042 - Crie um programa que leia o comprimento de três segmentos
# de reta e diga se elas podem formar um triângulo e além disso, qual é o tipo
# de triângulo formado:
#   ─ equilátero: todos os lados são iguais
#   ─ isósceles: dois lados iguais
#   ─ escaleno: todos os lados são diferentes.
# Klaudio Silva.

print('\033[33m-=-\033[m' * 10)
print('ANALISANDO TRIÂNGULOS v2.0'.center(30))
print('\033[33m-=-\033[m' * 10)

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if (seg1 + seg2 > seg3) and (seg1 + seg3 > seg2) and (seg2 + seg3 > seg1):
    # se os três lados são iguais
    if (seg1 == seg2) and (seg2 == seg3):
        print('Os segmentos acima PODEM FORMAR um triângulo \033[35mEQUILÁTERO\033[m.')
    # se somente dois lados são iguais
    elif (seg1 == seg2) or (seg1 == seg3) or (seg2 == seg3):
        print('Os segmentos acima PODEM FORMAR um triângulo \033[36mISÓSCELES\033[33m.')
    # nenhum lado é igual
    elif (seg1 != seg2) and (seg2 != seg3):
        print('Os segmentos acima PODEM FORMAR um triângulo \033[32mESCALENO\033[m.')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo!')
print()
