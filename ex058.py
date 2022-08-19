'''
Melhore o jogo do desafio 028 onde o computador
vai pensar em número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''

import random
from time import sleep
vencedor = False
tentativas = 0
computador = random.randint(0, 10)
print('Sou seu computador... \nAcabei de pensar em número entre 0 e 10. \nSerá que você consegue adivinhar qual foi?')

while not vencedor:
    jogador = int(input('Qual é seu palpite? '))
    tentativas += 1
    if computador > jogador:
        print('Mais... Tente mais uma vez.')
    elif computador < jogador:
        print('Menos... Tente mais uma vez.')
    else:
        print('PARABÉNS! Você venceu!')
        vencedor = True

print('Você precisou de {} tentativas para me vencer.'.format(tentativas))