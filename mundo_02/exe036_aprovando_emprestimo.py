# Python mundo 02
# Condições em Python - II
# Exercício 036 - Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar.
# ─ Calculeo valor da prestação mensal, sabendo que ela não pode exceder 30%
# do salário ou então o empréstimo será negado.
# Klaudio Silva.

# entrada de dados
casa = float(input('Qual é o valor da casa: R$'))
salario = float(input('Qual é o salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

# calculado valor das parcelas
totmes = anos * 12
parcela = casa / totmes

# apresentação dos resultados
print('Para pagar uma casa de R${:.2f} em {} anos as parcelas serão de  R${:.2f}.'.format(casa, anos, parcela))

if parcela > (salario * 30) / 100:
    print('\033[31mEmpréstimo NEGADO!\033[m')
else:
    print('\033[34mEmpréstimo CONCEDIDO!\033[m')
print()
