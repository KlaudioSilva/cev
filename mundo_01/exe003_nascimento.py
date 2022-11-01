# Python mundo 01
# Exercício 003 - Crie um script que leia o dia, o mês e o ano de nascimento
# de uma pessoa e mostre uma mensagem com a data formatada.
# Klaudio Silva.

# recebendo a data
dia = int(input('Digite qual foi o dia do seu nascimento: '))
mes = str(input('Digite o mês de seu nascimento: '))
ano = int(input('Por fim, digite o ano em que você nasceu: '))
print()

# exibinddo uma saída formatada
print('Você nasceu no dia {} do mês de {} no ano de {}.'.format(dia, mes, ano))
print()
