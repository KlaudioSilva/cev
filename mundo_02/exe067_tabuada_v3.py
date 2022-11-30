# Python mundo 02
# Repetições em Python - IV
# Exercício 067 - Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário. O programa será
# interrompido quando o número solicitado for negativo.

while True:
    print('-' * 40)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    
    if num < 0:  # encerrando o programa
        break

    for c in range(1, 11):
        # a tabuada usando fstrings
        print(f'{num:2} x {c:2} = {num * c:2}')