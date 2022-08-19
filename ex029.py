'''
Escreva um programa que leia a velocidade de um carro,

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada km acima do limite.
'''

velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h.')
    print('Você passou a {} km/h e deve pagar uma multa de R${:.2f}.'.format(velocidade, multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
