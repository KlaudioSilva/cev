# Python mundo 03
# Funções II em Python
# Exercício 105 - Faça um programa que tenha uma função notas(),
# que pode receber várias notas de alunos e vai retornar um 
# dicionário com as seguintes informações:
#   ─ quantidade de notas
#   ─ a maior nota
#   ─ a menor nota
#   ─ a média da turma
#   ─ a situação (opcional)
# Adicione também as docstrings da função.

def notas(*n, sit=False):
    """
        → Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma
    """
    r = {}  # criando um dicionário
    r['total'] = len(n) 
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)

    if sit:  # definindo a situação
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# programa principal
resp = notas(5.8, 3.4, 9.1, 4.9, sit=True)
print(resp)
# help(notas)