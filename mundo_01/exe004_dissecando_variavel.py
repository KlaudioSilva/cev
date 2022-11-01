# Python mundo 01
# Exercício 004 - Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações sobre ele.
# Klaudio Silva.

val = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(val))
print('Só tem espaços? ', val.isspace())
print('É um número? ', val.isnumeric())
print('É alfabético? ', val.isalpha())
print('É alfanumérico? ', val.isalnum())
print('Está tudo em maiúsculas? ', val.isupper())
print('Está tudo em minúsculas? ', val.islower())
print('Está capitalizado? ', val.istitle())
print()