# Python mundo 03
# Funções II em Python
# Exercício 104 - Crie um programa que tenha uma função chamada leiaint(),
# que vai funcionar de forma semelhante à função input() do Python, só que
# fazendo a validação para aceitar apenas um valor numérico.

print('-' * 30)

def leiaint(txt):
    ok = False  # inicia falso
    valor = 0   # por enquanto o valor é zero
    while True:
        n = str(input(txt))  # n recebe uma entrada
        if n.isnumeric():    # essa entrada é um número?
            valor = int(n)   # então converte para inteiro
            ok = True        # agora é verdadeiro
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:  # agora OK é verdadeiro
            break  # pare
    return valor   # retorne o valor que recebeu


# programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')