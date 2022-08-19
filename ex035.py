'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.

Condição de existência de um triângulo:
se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então,
eles podem formar um triângulo.
'''
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
    print('Os segmentos acima {}PODEM FORMAR{} um triângulo!'.format('\033[1;30;42m', '\033[m'))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} um triângulo!'.format('\033[1;30;41m', '\033[m'))