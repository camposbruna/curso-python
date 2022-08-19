'''
Faça um programa que leia 5 valores númericos
e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.
'''
listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-'*30)
print(f'Você digitou os valores {listanum}')

maior = max(listanum)
menor = min(listanum)

print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for c, v in enumerate(listanum):
    if maior == v:
        print(f'{c}.. ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for c, v in enumerate(listanum):
    if menor == v:
        print(f'{c}.. ', end='')
