def aumentar(num = 0, tax = 0, formato = False):  # função que aumenta o valor total em tantos %
    tot = num + (num * tax) / 100
    # retorne o total se o 'format' é false, senão retorne a moeda formatada
    return tot if not formato else moeda(tot)


def diminuir(num = 0, tax = 0, formato = False):  # função que diminue o valor total em tantos %
    tot = num - (num * tax) / 100
    return tot if not formato else moeda(tot)


def dobro(num = 0, formato = False):  # função que dobra o valor total
    tot = num * 2
    # obtendo o mesmo resultado mas escrevendo de outra forma
    return tot if formato is False else moeda(tot)


def metade(num = 0, formato = False):  # função que corta o valor total pela metade
    tot = num / 2
    return tot if formato is False else moeda(tot)


def moeda(num=0, moeda = 'R$'):  # função que formata o valor total como moeda BR
    # exibe o R$, o valor formatado com 2 casas decimais e troca o 'ponto' pela 'virgula'
    return f'{moeda}{num:.2f}'.replace('.', ',')
