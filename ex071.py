'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50,00 R$20,00 R$10,00 e R$1,00
'''

print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)
valor = int(input('Que valor você quer sacar? R$'))
valor_total = valor
cédula = 50
total_cédulas = 0

while True:
    if valor_total >= cédula:
        valor_total -= cédula
        total_cédulas += 1
    else:
        if total_cédulas > 0:
            print(f'Total de {total_cédulas} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        total_cédulas = 0
        if valor_total == 0:
            break
print('='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
