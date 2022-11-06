# Python mundo 01
# Usando Módulos
# Exercício 022 - Crie um programa que leia o nome completo de uma
# pessoa e mostre:
#   * o nome com todas as letras minúsculas
#   * o nome com todas as letras maiúsculas
#   * quantas letras têm ao todo sem considerar espaços
#   * quantas letras têm o primeiro nome.
# Klaudio Silva.

# recebendo o nome do usuário e eliminando espaços
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')

# fazendo as transformações
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))

# contado as letras sem os espaços
nome = nome.split()
nome2 = ''.join(nome)
print('Seu nome tem ao todo {} letras.'.format(len(nome2)))

# contando as letras do primeiro nome
nome3 = nome[0]
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome3, (len(nome3))))
print()
