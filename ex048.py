'''
Faça um programa que calcule a soma entre todos os
números ímpares que são múltiplos de três e
que se encontam no intervalo de 1 até 500
'''
s = 0
m = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        s += c
        m += 1
print('No intervalo 01 até 500 temos {} números multiplos de 3 e a soma entre eles é {}'.format(m, s))
