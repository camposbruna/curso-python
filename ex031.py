'''
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas.
'''

d = int(input('Informe a distância da sua viagem: '))
print('Você está prestes a começar uma viagem de {}km'.format(d))
preço = d * 0.5 if d <= 200 else d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))