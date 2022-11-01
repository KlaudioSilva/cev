# Python mundo 01
# Exercício 013 - Faça um algoritmo que leia o salário de um funcionário
# e mostre o seu novo salário com 15% de aumento.
# Klaudio Silva.

salario = float(input('Qual é o valor do seu salário atual? R$'))
novo = salario + (salario * 15) / 100

print('Com um aumento de 15%, seu salário passa a ser de R${:.2f}'.format(novo))
print()
