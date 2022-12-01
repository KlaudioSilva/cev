# Python mundo 03
# Tuplas em Python
# Exercício 077 - Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for cada in palavras:
    print(f'\nNa palavra {cada} temos: ', end='')
    for letra in cada:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print()
