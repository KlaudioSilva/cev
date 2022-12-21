# Python mundo 03
# Funções II em Python
# Exercício 102 - Crie um programa que tenha uma função fatorial(),
# que receba dois parâmetros: o primeiro que indica o número a calcular
# e o outro chamado 'show', que será um valor lógico (opcional) indicando
# se será mostrado ou não na tela o processo de calculo do fatorial.

def fatorial(num=1, show=True):
    """
        → Calcula o Fatorial de um número.
        :param num: o número a ser calculado.
        :param show: (opcional) mostrar ou não a conta.
        :return: o valor do Fatorial de um número
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print('-' * 40)
print(fatorial(5, show=False))
# help(fatorial)