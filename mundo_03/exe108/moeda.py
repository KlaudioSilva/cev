def aumentar(num = 0, tax = 0):  # função que aumenta o valor total em tantos %
    tot = num + (num * tax) / 100
    return tot


def diminuir(num = 0, tax = 0):  # função que diminue o valor total em tantos %
    tot = num - (num * tax) / 100
    return tot


def dobro(num = 0):  # função que dobra o valor total
    return num * 2


def metade(num = 0):  # função que corta o valor total pela metade
    return num / 2


def moeda(num=0, moeda = 'R$'):  # função que formata o valor total como moeda BR
    # exibe o R$, o valor formatado com 2 casas decimais e troca o 'ponto' pela 'virgula'
    return f'{moeda}{num:.2f}'.replace('.', ',')
