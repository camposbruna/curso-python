'''
Crie um programa que vai ler vários números e colocar em lista.
Depois disso, mostre:
a) Quantos números foram digitados;
b) A lista de valores ordenada de forma decrescente.
c) Se o valor 5 fpo digitado e está ou não na lista.
'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Valor inválido, digite novamente. Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('=-'*30)
print(f'Você digitou {len(valores)} elementos: {valores}')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}.')
if 5 in valores:
    print(f'O valor 5 faz parte da lista e está na posição {valores.index(5)}')
else:
    print(f'O valor 5 NÃO faz parte da lista!')
