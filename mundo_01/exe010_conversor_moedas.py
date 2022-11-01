# Python mundo 01
# Exercício 010 - Crie um programa que leia quanto dinheiro você têm na carteira
# e mostre quantos dolares você pode comprar. Use a cotação U$1,00 = R$3,27.
# Klaudio Silva.

carteira = float(input('Quanto você tem na carteira em R$: '))
dolar = carteira / 3.27

print('Com esses R${}, você poderá comprar um total de U${:.2f}'.format(carteira, dolar))
print()
