# Python mundo 01
# Exercício 008 - Escreva um programa que leia um valor em metros 
# e exiba convertido em centímetros e milímetros.
# Klaudio Silva.

metros = float(input('Digite um comprimento em metros [m]: '))
cent = metros * 100
mili = metros * 1000

print('O comprimento de {}ms convertido para: \nCentímetros é igual {}cm \nMilímetros é igual {}mm'.format(metros, cent, mili))
print()
