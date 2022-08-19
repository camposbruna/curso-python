'''
Crie um programa que vai ler vários números e colocar em lista.
Depois disso, crie duas listas extras que vão conter apneas
valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
lista_completa = []
lista_pares = []
lista_impares = []
while True:
    lista_completa.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Valor inválido. Digite novamente. Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for c, v in enumerate(lista_completa):
    if v % 2 == 0:
        lista_pares.append(v)
    else:
        lista_impares.append(v)
print('=-'*30)
print(f'A lista completa é {lista_completa}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impares}')
