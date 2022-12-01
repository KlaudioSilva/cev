# Python mundo 03
# Tuplas em Python
# Exercício 072 - Crie uma tupla que seja totalmente preenchinda
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))

# enquanto o usuário digitar um valor inválido
while (num > 20) or (num < 0):
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {cont[num]}')
print()
