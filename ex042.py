'''
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''
cores = {'reset':'\033[m',
         'yellow':'\033[33m',
         'red':'\033[31m',
         'green':'\033[32m',
         'blue':'\033[34m',
         'gray':'\033[1;37m'}

from time import sleep
print('-='*22)
print('{}Analisador de Triângulos{}'.format('\033[0;35m', '\033[m'))
print('-='*22)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('terceiro segmento: '))
print('CALCULANDO...')
sleep(.5)

if a < (b + c) and b < (a + c) and c < (a + b):
    if a == b == c:
        tipo_triangulo = 'Equilátero'
    elif a == b or b == c or a == c:
        tipo_triangulo = 'Isósceles'
    else:
        tipo_triangulo = 'Escaleno'
    print('Os segmentos acima {}FORMAM{} um {}Triângulo {}{}!'.format(cores['green'], cores['reset'], cores['blue'], tipo_triangulo, cores['reset']))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} um triângulo!'.format(cores['red'], cores['reset']))