def leiaDinheiro(txt):  # função que recebe uma entrada e valida se é um valor monetário
    valido = False
    while not valido:
        entrada = str(input(txt)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


'''
    ok = False  # no início o Ok é falso
    valor = 0  # inicialmente o valor é zero
    while True:
        n = str(input(txt)).strip()  # n recebe uma entrada e elimina espaços vazios
        if n.isnumeric():  # se a entrada é um número
            valor = float(n)  # converte para float
            ok = True  # ok para a ser verdadeiro
        else:
            print(f'\033[91mERRO: "{n}" é um preço inválido!\033[m')
        if ok:  # se ok é verdadeir encerra o loop
            break
    return valor  # retorne o valor recebido
'''