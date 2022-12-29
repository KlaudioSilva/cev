# Python mundo 03
# Erros e Exceções em Python
# Exercício 114 - Crie um código em Python que testa se o site
# 'pudim' está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mDeu erro!\033[m')
else:
    print('\033[34mTudo OK!\033[m')
