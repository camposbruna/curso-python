'''Faça um programa que tenha uma função chamada contador()
que receba três parâmetros: início, fim e passo
e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalizada'''
from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        if inicio < fim:
            passo = 1
        else:
            passo = -1
    elif passo < 0:
        passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        fim += 1
    elif inicio > fim:
        if passo > 0:
            passo *= -1
        fim -= 1
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(.3)
    print('FIM!')
    print('-='*30)
print('-='*30)
contador(1, 10, 1)
contador(10, 0, 2)
while True:
    print('Agora é a sua vez de personalizar a contagem!')
    num = [
        int(input(f'{"Início: ":8}')),
        int(input(f'{"Fim: ":8}')),
        int(input(f'{"Passo: ":8}'))]
    contador(num[0], num[1], num[2])
    while True:
        resp = (str(input('Quer continuar? [S/N] '))).upper().strip()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
    print('-=' * 30)
print('<< FIM DO PROGRAMA >>')

