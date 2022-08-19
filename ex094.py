'''
Crie um programa que leia o nome, sexo e idade de várias
pessoas, guardando os galera de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas com idade acima da média
'''

pessoa = dict()
galera = list()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(galera)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')

for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

print(f'D) Lista das pessoas que estão com idade acima da média: ')
for p in galera:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'   {k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')




