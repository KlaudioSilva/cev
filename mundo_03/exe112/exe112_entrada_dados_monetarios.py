# Python mundo 03
# Módulo e Pacotes em Python
# Exercício 112 - Dentro do pacote utilidadesCeV que criamos no
# exercício 111, temos um módulo chamado 'dado'.
# Crie uma função chamada leiaDinheiro(), que seja capaz de 
# funcionar como a função input(), mas com uma validação de dados
# para aceitar apenas valores que sejam monetários.

from utilidadesCev import moeda
from utilidadesCev import dado

valor = dado.leiaDinheiro('\033[36mDigite o preço: R$\033[m')
moeda.resumo(valor, 39, 57)