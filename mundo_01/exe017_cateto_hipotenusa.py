# Python mundo 01
# Exercício 017 - Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.
# Klaudio Silva.

catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
# Pitágoras: "A hipotenusa é igual a raiz quadrada da soma dos quadrados dos catetos"
hip = ((catop**2) + (catad**2)) ** (1/2)

print('O comprimento da hipotenusa desse triângulo retângulo é {:.2f}'.format(hip))
print()
