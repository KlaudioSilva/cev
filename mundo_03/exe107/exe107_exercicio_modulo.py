# Python mundo 03
# Módulo e Pacotes em Python
# Exercício 107 - Crie um módulo chamado de moeda.py que tenha
# as funções incorporadas: aumentar(), diminuir(), dobro() e 
# metade().
# Faça também o programa  que importe esse módulo e use alguma
# dessas funções.

import moeda
print('-' * 30)
valor = float(input('Digite o preço: R$'))
print(f'A metade de R${valor} é {moeda.metade(valor)}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'Aumentado 10%, temos R${moeda.aumentar(valor, 10)}')
print(f'Diminuido 15%, temos R${moeda.diminuir(valor, 15)}')