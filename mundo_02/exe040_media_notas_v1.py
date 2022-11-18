# Python mundo 02
# Condições em Python - II
# Exercício 040 - Crie um programa que leia as duas notas de um aluno e
# calcule a sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
#   * média abaixo de 5.0: Reprovado
#   * média entre 5.0 e 6.9: Recuperação
#   * média acima de 7.0: Aprovado.
# Klaudio Silva.

print('-' * 20)
print('CALCULANDO AS MÉDIAS')
print('-' * 20)

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print('Com as notas {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

# definindo aprovação, reprovação ou recuperação
if media >= 7:
    print('O aluno está APROVADO!')
elif (media >= 5) and (media <= 6.9):
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')
print()
