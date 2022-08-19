'''
Faça um programa que ajude um jogador da mega sena a criar palpites.
O programa vai perguntar quantos jogosserão gerados e vai
sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.
'''

from random import sample
from time import sleep
print('-'*35)
print('{:^35}'.format('JOGA NA MEGA SENA'))
print('-'*35)
qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f' SORTEANDO {qtd_jogos} JOGOS ', '=-'*3)
sleep(.5)
jogos = []
for c in range(0, qtd_jogos):
    jogos.append(sample(range(1, 60), 6))
    print(f'Jogo {c+1}: {sorted(jogos[c])}')
    sleep(.5)
print('{} < BOA SORTE! > {}'.format('-='*4, '=-'*4))
