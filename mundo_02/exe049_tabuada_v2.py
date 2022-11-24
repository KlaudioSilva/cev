# Python mundo 02
# Repetições em Python - II
# Exercício 049 - Refaça o exercício 09, mostrando a tabuada de
# um número que o usuário escolher, só que agora usando o laço FOR.
# Klaudio Silva.

num = int(input('Digite um número para ver a sua tabuada: '))

for c in range(1, 10 + 1):
    print('{} x {:2} = {:2}'.format(num, c, (num * c)))

print('Programa executado com sucesso!')
print()