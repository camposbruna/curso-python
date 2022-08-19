'''
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
'''

print('{:=^45}'.format(' SEQUÊNCIA DE FIBONACCI '))

termos = int(input('Quantos elementos você gostaria de mostrar? '))
c = 0
n1 = 0
n2 = 1

print('~'*45)
while c < termos:
    print(n1, end=' ➡ ')
    c += 1
    n3 = n1 + n2
    n1 = n2
    n2 = n3
print('FIM')
print('~'*45)

