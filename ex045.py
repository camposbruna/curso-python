'''
Crie um programa que faça o computador jogar jokenpô com você.
'''
from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('=-'*20)
print('JOKENPÔ')
print('=-'*20)

computador = randint(1, 3)
print('''Suas opções:
[1] Pedra
[2] Papel
[3] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(.5)
print('KEN')
sleep(.5)
print('PO!!!')
sleep(.5)

print('-='*15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 15)

if computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    elif jogador == 3:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 3:
    if jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR')
    elif jogador == 3:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
