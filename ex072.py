'''
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
mostra-lo por extenso.
'''

num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
               'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
               'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
               'dezessete', 'dezoito', 'dezenove', 'vinte')


continuar = 'S'
while continuar == 'S':
    while True:
        c = int(input('Digite um número entre 0 e 20: '))
        if 0 <= c <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {num_extenso[c]}.')
    while True:
        continuar = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
        if continuar == 'S' or continuar == 'N':
            break
        else:
            print('Valor inválido!')
if continuar == 'N':
    print('FIM DO PROGRAMA')
