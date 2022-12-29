def leiaInt(txt):  # função que verifica se o valor passado é um número inteiro
    while True:
        try:  # tratando erros de número não inteiros e usuário não digitar nada
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue  # joga de volta para o 'while'
        except KeyboardInterrupt:
            print('\n\033[36mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return num


def linha(tam = 42):  # simplesmente cria uma linha
    return '-' * 42


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):  # função que monta o cabeçalho do sistema
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:  # para cada item do menu
        print(f'\033[33m{c}\033[m ─ \033[34m{item}\033[m')  # exibir o número e o item
        c += 1
    print(linha())
    opc = leiaInt('\033[92mSua opção:\033[m ')
    return opc