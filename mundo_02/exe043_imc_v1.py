# Python mundo 02
# Condições em Python - II
# Exercício 043 - Crie um programa que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre se status de acordo com a tabela abaixo:
#   ─ abaixo de 18.5: abaixo do peso
#   ─ entre 18.5 e 25: peso ideal
#   ─ de 25 até 30: sobrepeso
#   ─ de 30 até 40: obesidade
#   ─ acima de 40: obesidade mórbida.
# Klaudio Silva.

# recebendo os dados
peso = float(input('Qual é o seu peso? [kg] '))
altura = float(input('Qual é a sua altura? [m] '))

# imc é igual ao peso dividido pela altura elevada ao quadrado
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}.'.format(imc))

# em que nível de imc você está inserido
if imc < 18.5:
    print('ATENÇÃO! Você está abaixo do peso.')
elif (imc >= 18.5) and (imc < 25):
    print('PARABÉNS! Você está dentro do peso ideal.')
elif (imc >= 25) and (imc < 30):
    print('Você está com SOBREPESO!')
elif (imc >= 30) and (imc < 40):
    print('Você está com OBESIDADE!')
else:
    print('CUIDADO! Você está em OBESIDADE MÓRBIDA!')
print()
