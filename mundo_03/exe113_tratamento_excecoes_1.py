# Python mundo 03
# Erros e Exceções em Python
# Exercício 113 - Reescreva a função leiaint() que fizemos na exercício
# 104, incluindo agora a possibilidade da digitação de um número de 
# tipo inválido.
# Aproveite e crie também a função leiafloat(), com a mesma funcionalidade.

print(f'\033[33m{"-" * 10} TRATAMENTO DE EXCEÇÕES {"-" * 10}\033[m')

def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue  # joga de volta para o 'while'
        except KeyboardInterrupt:
            print('\n\033[36mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return num


def leiaFloat(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido!')
            continue  # volta pro 'while'
        except KeyboardInterrupt:
            print('\n\033[36mO usuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return num


val1 = leiaInt('Digite um valor: ')
val2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {val1} e o real foi {val2}')
