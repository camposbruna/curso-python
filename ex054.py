'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
'''
from datetime import date
ano_atual = date.today().year
cont_maior = 0
cont_menor = 0
for c in range(1, 8):
    nascimento = int(input('Em que ano nasceu a {}º pessoa? '.format(c)))
    idade = ano_atual - nascimento
    if idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1
print('''\nAo todo tivemos {} pessoas maiores de idade
E também tivemos {} menores de idade.'''.format(cont_maior, cont_menor))
