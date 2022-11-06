# Python mundo 01
# Usando Módulos
# Exercício 024 - Crie um programa que leia o nome de uma cidade e
# diga se ela começa ou não com o nome 'Santo'.
# Klaudio Silva.

city = str(input('Em que cidade você nasceu? ')).strip()
# print('Santo' in city)    # usando o 'in' para encontrar a palavra
print(city[:5] == 'Santo')  # modelo do Guanabara
print()
