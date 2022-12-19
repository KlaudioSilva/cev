# Python mundo 03
# Funções I em Python
# Exercício 097 - Faça um programa que tenha uma função chamada 'escreva()',
# que receba um texto qualquer como parâmetro e mostre uma mensagem com
# um tamanho adaptável.

def escreva(txt):  # função para o texto
    print('~' * len(txt))  # calculando o tamanho do texto e gerando os simbolos
    print(txt)
    print('~' * len(txt))


# programa principal
escreva('  Klaudio Silva  ')
escreva('  Curso de Python em Vídeo  ')
escreva('  CeV  ')


'''
    No curso o Guanabara fez de uma forma um pouco diferente:

    def escreva(msg):
        tam = len(msg) + 4
        print('~' * tam)
        print(f'    {msg}')
        print('~' * tam)


    escreva('Gustavo Guanabara')
    escreva('Curso em Vídeo no Youtube')
    escreva('Cev')
'''