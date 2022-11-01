# Python mundo 01
# Exercício 015 - Crie um programa que pergunte a quantidade de quilômetros
# percorridos por um carro alugado e a quantidade de dias pelso quais ele
# foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15
# por quilômetro rodado.
# Klaudio Silva.

kms = int(input('Quantos quilômetros foram percorridos com esse carro? '))
dia = int(input('Por quantos dias o carro foi alugado? '))

totkm = kms * 0.15
totdia = dia * 60

print('O carro foi alugado por {} dias: totalizando R${:.2f}'.format(dia, totdia))
print('Nesse período foram rodados {} quilômetros: totalizando R${:.2f}'.format(kms, totkm))
print('O total geral dos custos com o aluguel do carro é de R${:.2f}'.format(totkm + totdia))
print()
