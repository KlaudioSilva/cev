# Python mundo 01
# Condições em Python
# Exercício 033 - Crie um programa que pergunte o salário de um funcionário
# e calcule o valor de seu aumento.
# Para salários superiores a R$1250,00 calcule um aumento de 10%. Para salários
# inferiores ou iguais, o aumento será de 15%.
# Klaudio Silva.

salario = float(input('Qual é o salário do funcionário? R$'))

# aumento de 10%
if salario > 1250:
    novo = salario + (salario * 10) / 100
    print('\033[34mQuem ganhava R$\033[93m{:.2f}\033[m \033[34mpassa a ganhar R$\033[93m{:.2f}\033[m \033[34magora.\033[m'.format(salario, novo))
# aumento de 15%
else:
    novo = salario + (salario * 15) / 100
    print('\033[34mQuem ganhava R$\033[93m{:.2f}\033[m \033[34mpassa a ganhar R$\033[93m{:.2f}\033[m \033[34magora.\033[m'.format(salario, novo))
print()
