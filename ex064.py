'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)
'''

soma = c = num = 0

while num != 999:
    c += 1
    soma += num
    num = int(input('Digite o {}º valor [999 para sair]: '.format(c)))
print('Total de números digitados: {}'.format(c - 1))
print('Soma total: {}'.format(soma))

