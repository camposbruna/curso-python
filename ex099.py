'''Faça um programa que tenha uma função chamada maior()
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer
qual deles é maior.'''
from time import sleep


def maior(*num):
    if num == ():
        cont = 0
        maior_valor = 0
    else:
        cont = len(num)
        maior_valor = max(num)
    print('=-' * 30)
    print('Analisando os valores passados...')
    for c in num:
        print(c, end=' ')
        sleep(.3)

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
