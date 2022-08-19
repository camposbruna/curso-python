'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

print('='*30)
print('{:^30}'.format('GERADOR DE PA'))
print('='*30)
pa = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0

while c < 10:
    c += 1
    print(pa, end=' ➡ ')
    pa += r
print('FIM DO PROGRAMA!')
