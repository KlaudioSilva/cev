# Python mundo 01
# Condições em Python
# Exercício 029 - Escreva um programa que leia a velocidade de um
# carro.
# Se ele ultrapassar 80kmh, mostre uma mensagem dizendo que ele foi
# multado.
# O custo da multa é de R$7,00 por cada kmh acima do limite.
# Klaudio Silva.

vel = int(input('Qual é a velocidade atual do carro? [Km/h]: '))

# se a velocidade exceder o limite aplique a multa
if vel > 80:
    multa = (vel - 80) * 7
    print('\033[91mMULTADO! Você excedeu o limite permitido que é de 80Km/h'
    '\nVocê deve pagar uma multa de\033[m \033[96mR${:.2f}!\033[m'.format(multa))
print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')
print()
