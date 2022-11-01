# Python mundo 01
# Exercício 012 - Faça um programa que leia o preço de um produto e
# mostre o seu novo preço com 5% de desconto.
# Klaudio Silva.

prec_atual = float(input('Qual é o preço atual desse produto: R$'))
prec_novo = prec_atual - (prec_atual * 5) / 100

print('Com um desconto de 5%, o preço de R${} passa a ser de R${:.2f}'.format(prec_atual, prec_novo))
print()
