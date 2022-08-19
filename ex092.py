'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário se por acaso o CTPS for
diferente de ZERO, o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar.
'''
from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - ano_nascimento
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['ctps'] == 0:
    for k, v in cadastro.items():
        print(f'  - {k} tem o valor {v}')
else:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - ano_nascimento
    print('=-'*30)
    print(cadastro)
    for k, v in cadastro.items():
        print(f'  - {k} tem o valor {v}')
