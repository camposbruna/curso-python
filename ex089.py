'''
Crie um programa que leia nome e duas notas de vários alunos
e guarte tudo em uma lista composta.
No final, mostre um boletim contendo a médi de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.
'''
cadastro = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    cadastro.append([nome, [nota1, nota2], média])

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp not in 'SN':
        resp = str(input('Valor inválido, digite novamente. Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        print('-=' * 30)
        print(f'{"Nº":<4}{"NOME":<20}{"MÉDIA":>6}')
        print('-' * 30)
        for i, a in enumerate(cadastro):
            print(f'{i:<4}{a[0]:<20}{a[2]:>6.1f}')
        print('-' * 30)
        break

while True:
    resp = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    if resp == 999:
        print('FINALIZANDO...')
        break
    if resp <= len(cadastro) -1:
        print(f'Notas de {cadastro[resp][0]} são {cadastro[resp][1]}')
        print('-'*30)
print('<<< VOLTE SEMPRE >>>')
