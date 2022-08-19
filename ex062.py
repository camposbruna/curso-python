'''
Melhore o desafio 061, perguntando para o usuário
se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

print('{:^30}'.format('GERADOR DE PA'))
print('-='*15)
pa = int(input('Primeiro termo: '))
r = int(input('Digite a razão: '))
c = 0
termos = 10
acrescenta_termos = 1

while acrescenta_termos != 0:
    while c < termos:
        print(pa, end=' ➡ ')
        c += 1
        pa += r
    print('PAUSA')
    acrescenta_termos = int(input('Quantos termos você quer mostrar a mais? '))
    termos += acrescenta_termos
print('A progressão foi finalizada com {} termos mostrados.'.format(termos))

