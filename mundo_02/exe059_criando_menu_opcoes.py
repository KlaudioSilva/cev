# Python mundo 02
# Repetições em Python - III
# Exercício 059 - Crie um programa que leia dois valores
# e mostre um menu na tela:
#   [ 1 ] somar
#   [ 2 ] multiplicar
#   [ 3 ] maior
#   [ 4 ] novos números
#   [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada
# em cada caso.

from time import sleep

opt = 0  # variável das opções do menu

print('=' * 18)
print('Menu de Opções'.center(18))
print('=' * 18)

# recebendo os valores
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

# gerando menu e recebendo as opções
while opt != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opt = int(input('>>> Qual é a sua opção? '))

    if opt == 1:  # fazer a soma
        print('A soma entre {} + {} é {}.'.format(num1, num2, (num1+num2)))
        print('=-=' * 10)
    elif opt == 2:  # fazer a multiplicação
        print('O resultado de {} x {} é {}.'.format(num1, num2, (num1*num2)))
        print('=-=' * 10)
    elif opt == 3:  # qual valor é o maior
        if num1 > num2:
            print('Entre {} e {} o maior valor é {}.'.format(num1, num2, num1))
        else:
            print('Entre {} e {} o maior valor é {}.'.format(num1, num2, num2))
        print('=-=' * 10)
    elif opt == 4:  # receber novos números
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        print('=-=' * 10)
    elif opt > 5:  # trantando opção inválida no menu
        print('Opção Inválida! Tente novamente.')
        print('=-=' * 10)

# encerrando o programa
print('Finalizando...')
sleep(0.5)  # aguarde 0.5 segundo
print('=-=' * 10)
print('Fim do programa! Volte sempre!')

print()
