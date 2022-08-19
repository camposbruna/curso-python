#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

#MÉTODO MATEMÁTICO TRADICIONAL
'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento o cateto adjacente: '))
hip = (co ** 2 + ca **2) ** (1/2)
print('A hipotenusa vai medir {}.'.format(hip))
'''


from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento o cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}.'.format(hypot(co, ca)))



