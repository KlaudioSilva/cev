# Python mundo 01
# Exercício 014 - Escreva um programa que converta uma temperatura
# digitada em graus Célcius para graus Fahrenheit.
# Klaudio Silva.

celcius = float(input('Digite qual é a temperatura em graus célcius [°C]: '))
fahrenheit = (celcius * 9 / 5) + 32

print('A temperatura de {}°C, convertida para fahrenheit é de {:.1f}°F'.format(celcius, fahrenheit))
print()
