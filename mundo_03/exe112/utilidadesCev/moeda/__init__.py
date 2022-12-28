def aumentar(num = 0, tax = 0, formato = False):  # função que aumenta o valor total em tantos %
    """
        → Calcula o aumento de um determinado preço,
        retornando o resultado com ou sem formatação.
        :param num: o preço que se quer reajustar
        :param tax: qual é a taxa de porcentagem do aumento
        :param formato: quer formatar a saída ou não?
        :return: o valor reajustado com ou sem formatação
    """
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


def moeda(num = 0, moeda = 'R$'):  # função que formata o valor total como moeda BR
    # exibe o R$, o valor formatado com 2 casas decimais e troca o 'ponto' pela 'virgula'
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num = 0, aum = 0, dim = 0):  # função que cria um resuminho com alterações no preço
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)

    print(f'Preço analisado: \t{moeda(num)}')  # valor total analisado
    print(f'Dobro do preço: \t{dobro(num, True)}')  # valor total dobrado
    print(f'Metade do preço: \t{metade(num, True)}')  # metade do valor total
    print(f'{aum}% de aumento: \t{aumentar(num, aum, True)}')  # valor total com um aumento %
    print(f'{dim}% de redução: \t{diminuir(num, dim, True)}')  # valor total com uma redução %
