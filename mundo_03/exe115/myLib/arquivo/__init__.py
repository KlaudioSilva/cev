from myLib.myInterf import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # 'rt' = leia o arquivo de texto
        a.close()  # fechar o arquivo
    except FileNotFoundError:  # se não encontrar o arquivo
        return False
    else:
        return True


def criarArquivo(nome):  # esta função cria o arquivo (caso ele não exista)
    try:
        a = open(nome, 'wt+')  # 'wt' = escreve arquivo texto  |  '+' vai criar o arquivo
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):  # esta função lê o arquivo e exibe seus dados
    try:
        a = open(nome, 'rt')  # abra e leia o arquivo
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:  # para cada linha em a?
            dado = linha.split(';')  # divida os dados pelo sinal de ';'
            dado[1] = dado[1].replace('\n', '')  # troque o contra-barra '\n' por um vazio
            print(f'{dado[0]:<30}{dado[1]:>3} anos')  # formatação para exibir os dados
    finally:
        a.close()


def cadastrar(arq, nome = 'desconhecido', idade = 0):  # esta função vai cadastrar uma nova pessoa no arquivo
    try:
        a = open(arq, 'at')  # abrindo o arquivo
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')  # escrevendo novos dados
        except:
            print('Houve um ERRO ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()