# Python mundo 01
# Usando Módulos
# Exercício 026 - Faça um programa que leia uma frase pelo
# teclado e mostre:
#   - quantas vezes aparece a letra 'a'
#   - em que posição aparece a primeira vez
#   - em que posição aparece a última vez
# Klaudio Silva.

frase = str(input('Digite uma frase: ')).upper().strip()

# analisando a frase
print('A letra "a/A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra "a/A" apareceu na posição {} da frase.'.format(frase.find('A')+1))
print('A última letra "a/A" apareceu na posição {} da frase.'.format(frase.rfind('A')+1))
print()
