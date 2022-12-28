# Python mundo 03
# Módulo e Pacotes em Python
# Exercício 110 - Adicione ao módulo moeda.py criado nos exercícios
# anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.

import moeda

valor = float(input('Digite o preço: R$'))
moeda.resumo(valor, 30, 15)