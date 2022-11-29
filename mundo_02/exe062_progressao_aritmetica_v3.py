# Python mundo 02
# Repetições em Python - III
# Exercício 062 - Melhore o exercício 061, perguntando ao usuário
# se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.

print('Gerador de PA v3.0'.center(20))
print('-=' * 10)

t1 = int(input('Primeiro termo da PA: '))
rz = int(input('Razão da PA: '))
cont = 1
termo = t1
tottermos = 0
mais = 10

while mais != 0:  # enquanto mais for diferente de 0
    tottermos = tottermos + mais  # tottermos recebe os valores que estão na variável mais
    while cont <= tottermos:
        print('{} → '.format(termo), end='')
        termo += rz
        cont += 1
    
    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(tottermos))
print()