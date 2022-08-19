#Faça um algoritimo que leia o prço de um produto e mostre seu novo preço, com 5% de desconto.

preçoInicial = float(input('Digite o preço do produto: R$'))
preçoFinal = preçoInicial * 0.95

print('O produto que custava R${:.2f}, na promoção  com desconto de 5% vai custar R${:.2f}.'.format(preçoInicial, preçoFinal))
