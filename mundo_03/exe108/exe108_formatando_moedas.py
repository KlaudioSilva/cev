# Python mundo 03
# Módulo e Pacotes em Python
# Exercício 108 - Adapte o código do exercício 107, criando uma função
# adicional chamada moeda(), que consiga mostrar os valores como um
# valor monetário formatado.

import moeda
print('=' * 30)
valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentado 10%, temos {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'Diminuido 15%, temos {moeda.moeda(moeda.diminuir(valor, 15))}')