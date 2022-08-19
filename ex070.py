'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra
b) Quantos produtos custam mais de R$1000,00
c) Qual é o nome do produto mais barato
'''
preço = total = tot_mil = menor_preço = c = 0
prod_barato = ' '
print('-'*45)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-'*45)
while True:
    produto = str(input('Nome do produto: ')).upper()
    preço = float(input('Preço: R$ '))
    c += 1
    total += preço
    if preço > 1000:
        tot_mil += 1
    if c == 1 or preço < menor_preço:
        menor_preço = preço
        prod_barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-' * 45)
    if resp == 'N':
        break
print(f'Total gasto na compra: R${total:.2f}')
print(f'Temos {tot_mil} produtos que custam mais de R$1000,00.')
print(f'O produto mais barato foi {prod_barato} que custa R${menor_preço:.2f}')


