# Python mundo 03
# Lista I em Python
# Exercício 083 - Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses.
# Seu programa deverá analisar se a expressão passada esta com os parênteses
# abertos e fechados na ordem correta.

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:  # para cada simb em expr:
    if simb == '(':  # se o simb for '(':
        pilha.append('(')  # a lista pilha recebe um '('
    elif simb == ')':  # se simb for igual ')':
        if len(pilha) > 0:  # se o tamanho da lista pilha for maior que 0:
            pilha.pop()  # elimine o último elemento da lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

print()
