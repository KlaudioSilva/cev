# Python mundo 01
# Exercício 006 - Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e a raiz quadrada.
# Klaudio Silva.

num = int(input('Digite um valor inteiro qualquer: '))
# usando variaveis
dob = num * 2
tri = num * 3
rzq = num ** (1/2)

print('O número {} tem: \nO dobro igual {} \nO triplo igual {} \nA raiz quadrada igual {}'.format(num, dob, tri, rzq))
print()
