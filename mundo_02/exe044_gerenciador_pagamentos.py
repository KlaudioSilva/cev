# Python mundo 02
# Condições em Python - II
# Exercício 044 - Elabore um programa que calcule o valor a ser pago por
# um produto, considerando o seu preço normal e a condição de pagamento:
#   ─ à vista dinheiro/cheque: 10% de desconto
#   ─ à vista no cartão: 5% de desconto
#   ─ em 2x no cartão: preço normal
#   ─ em 3x ou mais no cartão: 20% de juros.
# Klaudio Silva.

print('=' * 10, 'LOJAS SILVA', '=' * 10)

val = float(input('Preço total das compras: R$'))

# menu de opções de pagamento
print('FORMAS DE PAGAMENTO\n',
'[ 1 ] à vista dinheiro/cheque\n',
'[ 2 ] à vista no cartão\n',
'[ 3 ] 2x no cartão\n',
'[ 4 ] 3x ou mais no cartão')

opt = int(input('Qual é opção? '))

# valor final de acordo com a opção de pagamento escolhida
if opt == 1:
    tot = val - (val * 10) / 100
elif opt == 2:
    tot = val - (val * 5) / 100
elif opt == 3:
    tot = val
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(tot / 2))
elif opt == 4:
    tot = val + (val * 20) / 100
    parc = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(parc, (tot / parc)))
else:
    tot = val
    print('\033[31mERRO! Está opção é inválida!\033[m')

print('Valor da compra R${:.2f}, vai custar R${:.2f} no final.'.format(val, tot))
print()
