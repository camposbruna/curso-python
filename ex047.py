'''
Crie um programa que mostre na tela todos os números
pares que estão no intervalo entre 1 e 50.
'''

i = int(input('Valor inicial: '))
f = int(input('Valor final: '))
for c in range(i, f+1):
    if c % 2 == 0:
        print(c, end=' ')
