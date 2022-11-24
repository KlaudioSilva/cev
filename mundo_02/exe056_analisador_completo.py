# Python mundo 02
# Repetições em Python - II
# Exercício 056 - Crie um programa que leia o nome, a idade e o
# sexo de 4 pessoas. No final do programa mostre:
#   ─ a média de idade do grupo
#   ─ qual é o nome do homem mais velho
#   ─ quantas mulheres têm menos de 20 anos.

# variáveis
idades = 0
media = 0
hvelho = 0
hnome = ''
mulher20 = 0

# coletando os dados
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    idades += idade

    # encontrando o homem mais velho
    if (c == 1) and (sexo == 'M'):
        hvelho = idade
        hnome = nome
    else:
        if (idade > hvelho) and (sexo ==  'M'):
            hvelho = idade
            hnome = nome

    # quantas mulheres tem menos de 20
    if (sexo == 'F') and (idade < 20):
        mulher20 += 1

media = idades / 4

# dados finais
print('-' * 50)
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos de idade e se chama {}.'.format(hvelho, hnome))
print('Ao todo temos {} mulher(es) com menos de 20 anos.'.format(mulher20))
print()
