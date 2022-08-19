'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho;
- Quantas mulheres têm menos de 20 anos
'''
idade_acumulada = 0
mulheres = 0
idade_homens = 0
for c in range(1, 5):
    print('----- {:}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    idade_acumulada += idade
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M' and idade > idade_homens:
        idade_homens = idade
        homem_velho = nome
media = idade_acumulada / 4
print('\n- Média de idade do grupo: {} anos.'.format(media))
print('- O homem mais velho tem {} anos e se chama {}.'.format(idade_homens, homem_velho))
print('- Ao todo são {} mulheres com menos de 20 anos.' .format(mulheres))
