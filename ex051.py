'''
Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO
de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
i = int(input('Primeiro termo: '))
r = int(input('Digite a razão: '))
pa = i
for c in range(0, 10):
    print(pa, end=' ➡ ')
    pa += r
print('ACABOU!')