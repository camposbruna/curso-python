'''
Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
'''

números = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    while resp not in 'snSN':
        resp = str(input('Valor inválido. Digite novemente. Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('=-' * 20)
print(f'Você digitou os valores {sorted(números)}')
