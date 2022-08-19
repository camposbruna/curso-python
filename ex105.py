'''Faça um programa que tenha uma função notas() que
pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação(opcional)
Adicione também as docstrings da função'''


def notas(*n, sit=False):
    '''
    -> Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    aluno = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'média': sum(n)/len(n)
    }
    if sit:
        if aluno['média'] >= 7:
            aluno['situação'] = 'BOA'
        elif aluno['média'] >= 5:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


resp = notas(5.5, 5.5, 4, 3.5, 7, 4, sit=True)
print(resp)
