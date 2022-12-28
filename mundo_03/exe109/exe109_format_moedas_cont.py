# Python mundo 03
# Módulo e Pacotes em Python
# Exercício 109 - Modifique as funções que foram criadas no exercício 107
# para que elas aceitem um parâmetro a mais, informando se o valor retornado
# por elas vai ser ou não formatado pela função moeda(), desenvolvida no
# exercício 108.

import moeda
print('─' * 30)
valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentado 10%, temos {moeda.aumentar(valor, 10, True)}')
print(f'Diminuido 15%, temos {moeda.diminuir(valor, 15, True)}')