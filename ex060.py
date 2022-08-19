'''
Faça um programa que leua ym número qualquer e mostre o seu fatorial.
ex: 5! = 5x4x3x2x1=120
fatorial = 1
num = int(input('Digite um número: '))
for c in range(num, 0, -1):
    fatorial = fatorial * c
    print(c, end=' x ')
print('= {}'.format(fatorial))
'''
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))
