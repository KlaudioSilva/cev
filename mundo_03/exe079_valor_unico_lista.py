# Python mundo 03
# Lista I em Python
# Exercício 079 - Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele
# não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

valores = []
num = ''
res = 'SN'

while True:
    num = int(input('Digite um valor: '))
    if num in valores:  # se o valor já existir na lista, não adicionar
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    
    # vai continuar?
    res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Resposta inválida! Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break

print('-=-' * 15)
print(f'Você digitou os valores {valores}')
print()