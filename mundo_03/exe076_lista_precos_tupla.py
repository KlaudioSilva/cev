# Python mundo 03
# Tuplas em Python
# Exercício 076 - Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.90, 'Mochila', 120, 'Canetas', 22.30,'Livro', 34.90)

print('-' * 40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-' * 40)

for item in range(0, len(listagem)):
    if item % 2 == 0:
        # na formatação  ':.<30' é para alinhar a esquerda com 30 espaços e inserir os pontinhos
        print(f'{listagem[item]:.<30}', end='')
    else:
        # na formatação ':>7' é o alinhamento a direita com 7 espaços, o '.2f' é para casa decimal
        print(f'R${listagem[item]:>7.2f}')