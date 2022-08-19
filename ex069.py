'''
Crie um programa que leia a idade e o sexo de várias pessoas. A casa pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
a) quantas pessoas tem mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres tem menos de 20 anos
'''

idade = cont_mulheres = cont_homens = maiores_idade = 0
while True:
    continuar = sexo = ' '
    print('-'*40)
    print('{:^40}'.format('CADASTRE UMA PESSOA'))
    print('-'*40)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        maiores_idade += 1
    if sexo == 'M':
        cont_homens += 1
    if sexo == 'F' and idade < 20:
        cont_mulheres += 1
    print('-' * 40)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        break
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas com mais de 18 anos: {maiores_idade}')
print(f'Ao todo temos {cont_homens} homens cadastrados')
print(f'E temos {cont_mulheres} mulheres com menos de 20 anos')

