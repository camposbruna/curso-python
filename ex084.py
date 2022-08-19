'''
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves
'''
dados = []
cadastro = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    cadastro.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Valor inválido! Digite novamente. Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-'*30)
print(f'Ao todo, você cadastrou {len(cadastro)} pessoas.')

maior_peso = cadastro[0][1]
menor_peso = cadastro[0][1]
for p in cadastro:
    if p[1] > maior_peso:
        maior_peso = p[1]
    if p[1] < menor_peso:
        menor_peso = p[1]

pessoa_pesada = []
pessoa_leve = []
for p in cadastro:
    if p[1] >= maior_peso:
        pessoa_pesada.append(p[0])
    if p[1] <= menor_peso:
        pessoa_leve.append(p[0])

print(f'O maior peso foi de {maior_peso}kg. Peso de {pessoa_pesada}')
print(f'O menor peso foi de {menor_peso}kg. Peso de {pessoa_leve}')
