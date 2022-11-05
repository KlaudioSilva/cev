# Python mundo 01
# Exercício 018 - Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# Klaudio Silva.

from math import cos, sin, tan, radians  
ang = float(input('Digite o ângulo que você deseja: '))

# No Python os graus são em radianos. Então vamos fazer a conversão:
rad = radians(ang)
print('O ângulo de {}º tem o SENO de {:.2f}'.format(ang, sin(rad)))
print('O ângulo de {}º tem o COSSENO de {:.2f}'.format(ang, cos(rad)))
print('O ângulo de {}º tem a TANGENTE de {:.2f}'.format(ang, tan(rad)))
print()
