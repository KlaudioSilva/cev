# Python mundo 02
# Repetições em Python - III
# Exercício 065 - Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos os valores e
# qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário
# se ele quer continuar ou não, digitando valores.

tot = 0
med = 0
som = 0
maior = 0
menor = 0

resp = 'SN'
# estrutura para receber os números e decidir se continua
while resp not in 'N':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    tot += 1
    som = som + num

    # descobrindo o maior e o menor
    if tot == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

# apresentação dos dados finais
print(f'Você digitou {tot} números e a média foi {som/tot}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
print()
