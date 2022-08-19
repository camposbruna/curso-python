'''
Faça um programa que leia nome e média
de um aluno, guardando também a situação em
um dicionário. No final, mostre o conteúdo da estrutura
na tela.
'''
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['média'] = float(input(f'Média de {cadastro["nome"]}: '))
if cadastro['média'] >= 7:
    cadastro['situação'] = 'Aprovado'
elif 5 <= cadastro['média'] < 7:
    cadastro['situação'] = 'Recuperação'
else:
    cadastro['situação'] = 'Reprovado'
print('-='*30)
for k, v in cadastro.items():
    print(f'- {k} é igual a {v}')
