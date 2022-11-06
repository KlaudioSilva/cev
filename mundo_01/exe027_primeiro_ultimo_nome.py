# Python mundo 01
# Usando Módulos
# Exercício 027 - Crie um programa que leio o nome completo de uma
# pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Klaudio Silva.

nome = str(input('Digite seu nome completo: '))
print('Muito prazer em te conhecer!')

# separando os nomes
nome2 = nome.split()
print('Seu primeiro nome é {}.'.format(nome2[0]))
print('Seu último nome é {}.'.format(nome2[len(nome2)-1]))
print()
