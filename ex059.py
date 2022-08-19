'''
Crie um programa que leia dos valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
opção = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while opção != 5:
    print('-'*40)
    print('''Qual operação você deseja fazer?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('Opção selecionada: '))
    print('-' * 40)

    if opção == 1:
        print('O resultado de {} + {} é igual a {}.'.format(n1, n2, n1 + n2))
    elif opção == 2:
        print('O resultado de {} x {} é igual a {}.'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opção == 5:
        print('FINALIZANDO...')
        sleep(1)
        print('-'*40)
        print('Fim do programa! Volte Sempre')
    else:
        print('Opção inválida. Tente novamente.')

