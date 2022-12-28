# Python mundo 03
# Módulo e Pacotes em Python
# Exercício 111 - Crie um pacote chamado utilidadesCeV que tenha
# dois módulos internos chamados 'moeda' e 'dado'.
# Transfira todas as funções utilizadas nos exercícios 107, 108 e
# 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadesCev import moeda

valor = float(input('Digite o preço: R$'))
moeda.resumo(valor, 39, 57)