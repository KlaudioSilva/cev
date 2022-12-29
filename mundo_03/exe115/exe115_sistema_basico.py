# Python mundo 03
# Erros e Exceções em Python
# Exercício 113 - Crie um pequeno sistema modularizado que
# permita cadastrar pessoas pelo seu nome e idade em um
# arquivo de texto simples.
# O sistema só vai ter 2 opções: casdastrar uma nova pessoa
# e listar as pessoas cadastradas.

from time import sleep
from myLib.myInterf import *  # importando as funções para criar o menu
from myLib.arquivo import *

arq = 'cursopython.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

# sistema
while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # opção para sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)