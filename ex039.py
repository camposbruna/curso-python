'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-> Se ele ainda vai se alistar ao serviço militar
-> Se é a hora de se alistar
-> Se jjá passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
'''

from datetime import date


sexo = str(input('Informe o seu sexo [M] [F]: ')).upper()

if sexo == 'M':
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print('Que nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))
    if idade < 18:
        print('Faltam {} anos para você se alistar. \nSeu alistamento será em {}.'.format(18 - idade, ano_nascimento + 18))
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos. \nSeu alistamento foi em {}.'.format(idade - 18, ano_nascimento + 18))
    else:
        print('VALOR INVÁLIDO!')
elif sexo == 'F':
    print('Alistamento OPCIONAL.')
