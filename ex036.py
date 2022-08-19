'''
Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar:
-> o valor da casa
-> o salário do compreador
-> quantos anos ele vai pagar.

Calcule:
-> valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''
cores = {'reset':'\033[m',
         'yellow':'\033[33m',
         'red':'\033[31m',
         'green':'\033[32m'}

print('=-='*20)
print('Análise de Crédito para compra de imóvel')
print('=-='*20)
imóvel = float(input('Qual o valor do imóvel? R$ '))
salário = float(input('Qual o salário do comprador? R$'))
tempo = int(input('Em quantos anos você pretende pagar? '))

parcelas = imóvel / (tempo * 12)
print('Para pagar uma casa de {}R${:.2f}{}, a prestação será de {}R${:.2f}{}'.format(cores['yellow'], imóvel, cores['reset'], cores['yellow'], parcelas, cores['reset']))

if parcelas > salário * 0.3:
    print('{}EMPRÉSTIMO NEGADO!{}'.format(cores['red'], cores['reset']))
else:
    print('{}EMPRÉSTIMO APROVADO!{}'.format(cores['green'], cores['reset']))
