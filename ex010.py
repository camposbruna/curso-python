#Crie um programa que leia quanto dinherio uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Consiedere 1 dólar = 3,27 reais

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 3.27

print('Com R${:.2f} você pode comprar U${:.2f}.'.format(real, dolar))
