# Python mundo 01
# Exercício 011 - Faça um programa que leia a largura e a altura de uma parede em
# metros, calcule a sua área em metros quadrados e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
# Klaudio Silva.

# recebendo os dados
lar = float(input('Qual é a largura da parede em metros? '))
alt = float(input('Qual é a altura da parede em metros? '))

# calculando
area = lar * alt
tinta = area / 2

# exibindo informações
print('Com a largura de {}m e altura de {}m, essa parede tem uma área de {}m².'.format(lar, alt, area))
print('Para pintar essa área serão necessários {}lts de tinta.'.format(tinta))
print()
