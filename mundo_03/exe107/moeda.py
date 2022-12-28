def aumentar(num, tax):  # função que aumenta o valor total em tantos %
    tot = num + (num * tax) / 100
    return tot


def diminuir(num, tax):  # função que diminue o valor total em tantos %
    tot = num - (num * tax) / 100
    return tot


def dobro(num):  # função que dobra o valor total
    return num * 2


def metade(num):  # função que corta o valor total pela metade
    return num / 2
