#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cossemo e tangente desse ângulo.

from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo: '))
seno = sin(radians(ângulo))
coseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo {:.2f}º tem seno = {:.2f}, cosseno = {:.2f} e tangente = {:.2f}'.format(ângulo, seno, coseno, tangente))
