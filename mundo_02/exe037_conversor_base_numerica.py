# Python mundo 02
# Condições em Python - II
# Exercício 037 - Crie um programa que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# ─ 1 para binário
# ─ 2 para octal
# ─ 3 para hexadecimal.
# Klaudio Silva.

num = int(input('Digite um número inteiro: '))

# criando menu de opções
print('Escolha uma das bases para conversão:\n',
'[ 1 ] converter para BINÁRIO\n',
'[ 2 ] converter para OCTAL\n',
'[ 3 ] converter para HEXADECIMAL')

opt = int(input('Sua opção: '))

# realizando as conversões
if opt == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opt == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opt == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mERRO!\033[m Essa opção é inválida!')
print()
