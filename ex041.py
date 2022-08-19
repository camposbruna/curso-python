'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
'''
from datetime import date
nascimento = int(input('Digite o ano de nascimeto: '))
ano = date.today().year
idade = ano - nascimento
categoria = ''

if 0 < idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print('''Ano de nascimento: {}
O atleta tem {} anos
Classificação: {}'''.format(nascimento, idade, categoria))
